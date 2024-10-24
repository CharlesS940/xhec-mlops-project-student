import pickle
from pathlib import Path
from prefect import task, flow


@task
def pickle_object(obj, filename: str, directory: str = ""):
    """Pickle a Python object and save it to a file."""
    path = Path(directory)
    path.mkdir(parents=True, exist_ok=True)
    file_path = path / f"{filename}"

    with open(file_path, "wb") as file:
        pickle.dump(obj, file)

    print(f"Object saved to {file_path}")
