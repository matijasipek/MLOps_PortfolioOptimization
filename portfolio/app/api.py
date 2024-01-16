from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import os
import shutil
import asyncio
from src.predict_model import predict
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter, Gauge, Histogram, generate_latest
import time

app = FastAPI()

#directory to store temporary uploaded files
upload_dir = "./uploads"
os.makedirs(upload_dir, exist_ok=True)

# Prometheus metrics
custom_counter = Counter('custom_event_count', 'Count of custom events')
successful_predictions_counter = Counter('successful_predictions_count', 'Count of successful predictions')
failed_predictions_counter = Counter('failed_predictions_count', 'Count of failed predictions')
prediction_duration = Histogram('prediction_duration_seconds', 'Duration of prediction process in seconds')
prediction_size_gauge = Gauge('prediction_file_size_bytes', 'Size of prediction file uploaded')

# Record a custom event
def record_custom_event():
    custom_counter.inc()

# Instrumentator setup with custom metrics
instrumentator = Instrumentator()

instrumentator.add(({
"custom_event_count": custom_counter,
"successful_predictions_count": successful_predictions_counter,
"failed_predictions_count": failed_predictions_counter,
"prediction_duration_seconds": prediction_duration,
"prediction_file_size_bytes": prediction_size_gauge
}))


@app.post("/predict/")
async def predict_file(file: UploadFile):
    try:
        # Record the start time before making the prediction
        start_time = time.time()

        #checkign if the file is a CSV file
        if not file.filename.endswith(".csv"):
            raise HTTPException(status_code=400, detail="Uploaded file must be in CSV format.")

        #unique file path in the upload directory
        file_path = os.path.join(upload_dir, file.filename)
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        #calling predict function from predict_model.py with the file_path as input
        prediction_results = await asyncio.to_thread(predict, file_path)

        # Calculate the duration in seconds
        end_time = time.time()
        duration_seconds = end_time - start_time

        # Increment successful predictions count
        successful_predictions_counter.inc()

        # Observe the duration of the prediction process
        prediction_duration.observe(duration_seconds)  

        # Set the prediction file size in bytes
        prediction_size_gauge.set(os.path.getsize(file_path))

        #returning the prediction results as JSON response
        return JSONResponse(content={"predictions": prediction_results})

    except Exception as e:
        failed_predictions_counter.inc() # Increment failed predictions count
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/metrics")
async def get_metrics():
    return JSONResponse(content=generate_latest())

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


Instrumentator().instrument(app).expose(app)