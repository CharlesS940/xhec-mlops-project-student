import pandas as pd
from predicting import predict_age
from training import train_model
from utils import pickle_object
from preprocessing import preprocess_data
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

    # 2. Preprocess the new input data
    X_train_scaled, X_test_scaled, y_train, y_test = preprocess_data(new_data_path)

    X = pd.concat([X_train_scaled, X_test_scaled])

    # 3. Predict using the loaded model
    predictions = predict_age(X)
    print(f"Predictions: {predictions}")

    existing_data_path = "data/abalone.csv"

    # 4. Load the full dataset for retraining
    full_data = load_dataset(existing_data_path, new_data_path)

    # 5. Overwrite the existing data with the full dataset
    full_data.to_csv(existing_data_path, index=False)

    # 5. Retrain the model on the full dataset
    updated_model = train_model(X_train_scaled, X_test_scaled, y_train, y_test)

    # 6. Save the newly trained model
    pickle_object(updated_model, "src/web_service/local_objects/abalone_age_model.pkl")

    return predictions


@task
def load_dataset(existing_data_path: str, new_data_path: str) -> pd.DataFrame:
    """Load and append new data to existing data."""
    existing_data = pd.read_csv(existing_data_path)
    new_data = pd.read_csv(new_data_path)

    # Combine the datasets
    combined_data = pd.concat([existing_data, new_data], ignore_index=True)
    return combined_data


if __name__ == "__main__":
    batch_predict_and_retrain_workflow(new_data_path="data/new_data.csv")
