<div align="center">

# xhec-mlops-project-student

[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10-blue.svg)]()
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Linting: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-informational?logo=pre-commit&logoColor=white)](https://github.com/artefactory/xhec-mlops-project-student/blob/main/.pre-commit-config.yaml)

</div>

## Project Description

This repository aims to industrialize the [Abalone age prediction](https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset) Kaggle contest. The goal is to predict the age of abalone (column "Rings") from physical measurements ("Shell weight", "Diameter", etc.). The project involves creating workflows to train and retrain models, deploying these workflows using Prefect, and providing an API for making predictions on new data.

## Directory Structure

- `src/`: Contains the source code for the project.
  - `modelling/`: Contains scripts for training and retraining the model.
  - `api/`: Contains the FastAPI application for making predictions.
- `data/`: Contains the dataset used for training and predictions.
- `requirements.txt`: Lists the dependencies required for the project.
- `requirements-dev.txt`: Lists the development dependencies.
- `environment.yml`: Conda environment configuration file.

## Participants

Tess Coullon (tesscln)
Charles Siret (CharlesS940)
Gaspard Hassenforder (Gaspard0302)
Henri Vignial (hvignial)
Raphaël Amzallag (raphaelamzallag)

## Setting Up the Virtual Environment

1. Create a virtual environment:

    ```bash
    python -m venv <your_venv_name>
    ```

    If Python 3.10 or 3.11 is not your default version, specify the version:

    ```bash
    py -3.10 -m venv <your_venv_name>
    ```

2. Activate the virtual environment and install the requirements:

    ```bash
    <your_venv_name>\Scripts\activate.ps1
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    ```

3. Install `pip-tools` to use `pip-compile` for generating [requirements.txt](http://_vscodecontentref_/#%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fraphaelamzallag%2Fcode%2Fmasters%2Fhec%2Fmlops%2Fxhec-mlops-project-student%2Frequirements.txt%22%2C%22path%22%3A%22%2FUsers%2Fraphaelamzallag%2Fcode%2Fmasters%2Fhec%2Fmlops%2Fxhec-mlops-project-student%2Frequirements.txt%22%2C%22scheme%22%3A%22file%22%7D%7D):

    ```bash
    pip install pip-tools
    ```

## Running the API

1. Navigate to the root directory of the project.

2. Run the FastAPI app with uvicorn:

    ```bash
    uvicorn src.web_service.main:app --host 0.0.0.0 --port 8000
    ```

## Running the API with Docker

1. Build the Docker image:

    ```bash
    docker build -t abalone-age-api .
    ```

2. Run the Docker container:

    ```bash
    docker run -p 8000:8000 -p 4201:4201 abalone-age-prediction   
    ```
