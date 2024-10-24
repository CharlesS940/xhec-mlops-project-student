import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler


def load_and_preprocess_data(file_path):
    # Load dataset
    df = pd.read_csv(file_path)

    # Convert Rings to Age
    df["Age"] = df["Rings"] + 1.5

    # Drop the Rings column as it's no longer needed
    df = df.drop(columns=["Rings"])

    # Encode the 'Sex' column
    label_encoder = LabelEncoder()
    df["Sex"] = label_encoder.fit_transform(df["Sex"])

    # Define features and target
    X = df.drop(columns=["Age"])
    y = df["Age"]

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Standardize the feature data
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test
