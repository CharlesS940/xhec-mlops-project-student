import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from utils import pickle_object

def train_and_log_model(X_train_scaled, X_test_scaled, y_train, y_test):
  # Initialize the model
    model = RandomForestRegressor(random_state=42)

    # Train the model
    model.fit(X_train_scaled, y_train)

    # Make predictions
    y_pred = model.predict(X_test_scaled)

    # Evaluate the model
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)


    # Infer the model signature
    signature = infer_signature(X_train_scaled, model.predict(X_train_scaled))

    print(f"MAE: {mae}, R2 Score: {r2}")

    # Pickle the model
    pickle_object(model, "abalone_age_model")
