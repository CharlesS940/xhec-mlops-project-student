import pickle
from pathlib import Path


def pickle_object(obj, filename: str, directory: str = "src/web_service/local_objects"):
    """Pickle a Python object and save it to a file."""
    path = Path(directory)
    path.mkdir(parents=True, exist_ok=True)
    file_path = path / f"{filename}.pkl"

    with open(file_path, "wb") as file:
        pickle.dump(obj, file)

    print(f"Object saved to {file_path}")
