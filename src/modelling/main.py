import argparse
from pathlib import Path
from preprocessing import load_and_preprocess_data
from training import train_and_log_model

def main(trainset_path: Path) -> None:
  """Train a model using the data at the given path and save the model (pickle)."""
  # Read and preprocess data
  X_train_scaled, X_test_scaled, y_train, y_test = load_and_preprocess_data(trainset_path)

  # Train model and log with MLflow
  train_and_log_model(X_train_scaled, X_test_scaled, y_train, y_test)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Train a model using the data at the given path.")
  parser.add_argument("trainset_path", type=str, help="Path to the training set")
  args = parser.parse_args()
  main(Path(args.trainset_path))
