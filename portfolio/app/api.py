from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import os
import shutil
import asyncio
from src.predict_model import predict

app = FastAPI()

#directory to store temporary uploaded files
upload_dir = "./uploads"
os.makedirs(upload_dir, exist_ok=True)

@app.post("/predict/")
async def predict_file(file: UploadFile):
    try:
        #checkign if the file is a CSV file
        if not file.filename.endswith(".csv"):
            raise HTTPException(status_code=400, detail="Uploaded file must be in CSV format.")

        # unique file path in the upload directory
        file_path = os.path.join(upload_dir, file.filename)
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        #calling predict function from predict_model.py with the file_path as input
        prediction_results = await asyncio.to_thread(predict, file_path)

        #returning the prediction results as JSON response
        return JSONResponse(content={"predictions": prediction_results})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


