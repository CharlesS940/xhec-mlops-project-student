import pickle

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from prefect import task, flow


@task
def load_model(model_path: str = "src/web_service/local_objects/abalone_age_model.pkl"):
    """Load the pickled model."""
    with open(model_path, "rb") as file:
        model = pickle.load(file)
    return model


def prepare_input(
    sex: str,
    length: float,
    diameter: float,
    height: float,
    whole_weight: float,
    shucked_weight: float,
    viscera_weight: float,
    shell_weight: float,
):
    """Prepare input data for prediction."""
    data = pd.DataFrame(
        {
            "Sex": [sex],
            "Length": [length],
            "Diameter": [diameter],
            "Height": [height],
            "Whole weight": [whole_weight],
            "Shucked weight": [shucked_weight],
            "Viscera weight": [viscera_weight],
            "Shell weight": [shell_weight],
        }
    )

    le = LabelEncoder()
    le.fit(["M", "F", "I"])
    data["Sex"] = le.transform(data["Sex"])

    feature_names = [
        "Sex",
        "Length",
        "Diameter",
        "Height",
        "Whole weight",
        "Shucked weight",
        "Viscera weight",
        "Shell weight",
    ]

    return data[feature_names].values


@task
def predict_age(features):
    """
    Predict abalone age using the trained model.
    Returns dictionary with predicted age and rings.
    """
    model = load_model()
    age_prediction = model.predict(features)[0]
    rings = age_prediction - 1.5

    return {
        "predicted_age": round(age_prediction, 2),
        "predicted_rings": round(rings, 2),
    }
