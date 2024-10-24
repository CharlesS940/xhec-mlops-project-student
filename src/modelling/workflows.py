import pandas as pd
from .predicting import predict
from .training import train_model
from .utils import pickle_object
from .preprocessing import preprocess_data
from prefect import task, flow
import pickle
import os


@flow
def batch_predict_and_retrain_workflow(new_data_path: str):
    """
    1. Predict with current model.
    2. Retrain model on full dataset including new data.
    3. Update model for future predictions.
    """

    # 1. Load the current model
    model = load_model("../web_service/local_objects/abalone_age_model.pkl")

    # 2. Preprocess the new input data
    processed_data = preprocess_data(new_data_path)

    # 3. Predict using the loaded model
    predictions = predict(model, processed_data)
    print(f"Predictions: {predictions}")

    existing_data_path = "../../data/abalone.csv"

    # 4. Load the full dataset for retraining
    full_data = load_dataset(existing_data_path, new_data_path)

    # 5. Retrain the model on the full dataset
    updated_model = train_model(
        full_data, target_column="target"
    )  # Specify the correct target column

    # 6. Save the newly trained model
    pickle_object(updated_model, "src/web_service/local_objects/abalone_age_model.pkl")

    return predictions


@task
def load_model(model_filepath: str):
    """Load a model from a pickle file with error handling.

    Args:
        model_filepath (str): The path to the model file.

    Returns:
        The loaded model or None if loading fails.
    """
    if not os.path.exists(model_filepath):
        print(f"Model file not found: {model_filepath}")
        return None

    try:
        with open(model_filepath, "rb") as file:
            model = pickle.load(file)
        return model
    except Exception as e:
        print(f"Failed to load model: {e}")
        return None


@task
def load_dataset(existing_data_path: str, new_data_path: str) -> pd.DataFrame:
    """Load and append new data to existing data."""
    existing_data = pd.read_csv(existing_data_path)
    new_data = pd.read_csv(new_data_path)

    # Combine the datasets
    combined_data = pd.concat([existing_data, new_data], ignore_index=True)
    combined_data.to_csv("../../data/abalone.csv", index=False)
    return combined_data
