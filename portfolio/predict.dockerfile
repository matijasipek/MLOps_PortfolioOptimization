# Base image
FROM python:3.10-slim
# install python, git, and required libraries
RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc git libopenblas-dev liblapack-dev cmake && \
    apt clean && rm -rf /var/lib/apt/lists/*
###  copy folder
COPY requirements.txt requirements.txt
COPY pyproject.toml pyproject.toml 
COPY src/ src/
COPY data/ data/
COPY visualizations/ visualizations/
COPY models/ models/
COPY notebooks/ notebooks/
# Ensure the processed directory exists and copy the X_test.csv file into it
RUN mkdir -p /data/processed
COPY uploads/X_test.csv /data/processed/X_test.csv

#  environment variables
ENV RUNNING_IN_DOCKER=true

# install python dependencies
WORKDIR /
RUN pip install -r requirements.txt --no-cache-dir
RUN pip install git+https://github.com/skfolio/skfolio.git --no-cache-dir
RUN pip install . --no-deps --no-cache-dir

# Expose port 8000 for Prometheus metrics
EXPOSE 8000

# prediction script
CMD ["python", "-u", "src/predict_model.py", "/data/processed/X_test.csv"]