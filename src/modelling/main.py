import argparse
from pathlib import Path
from preprocessing import load_data, preprocess_data
from training import train_and_log_model
from prefect import task, flow


@flow
def main(trainset_path: Path) -> None:
    """Train a model using the data at the given path and save the model (pickle)."""
    # Read and preprocess data
    df = load_data(trainset_path)
    X_train_scaled, X_test_scaled, y_train, y_test = preprocess_data(df)

    # Train model and log with MLflow
    train_and_log_model(X_train_scaled, X_test_scaled, y_train, y_test)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Train a model using the data at the given path."
    )
    parser.add_argument("trainset_path", type=str, help="Path to the training set")
    args = parser.parse_args()
    main(Path(args.trainset_path))
