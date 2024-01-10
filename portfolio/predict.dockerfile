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
COPY reports/ reports/
COPY models/ models/
COPY notebooks/ notebooks/
COPY reports/ reports/

# install python dependencies
WORKDIR /
RUN --mount=type=cache,target=~/pip/.cache pip install -r requirements.txt --no-cache-dir
RUN pip install git+https://github.com/skfolio/skfolio.git --no-cache-dir
RUN pip install . --no-deps --no-cache-dir

# prediction script
ENTRYPOINT ["python", "-u", "src/predict_model.py"]