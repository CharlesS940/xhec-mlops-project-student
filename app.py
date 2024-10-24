from fastapi import FastAPI
from pydantic import BaseModel
from src.modelling.predicting import prepare_input, predict_age

app = FastAPI()

class AbaloneFeatures(BaseModel):
  sex: str
  length: float
  diameter: float
  height: float
  whole_weight: float
  shucked_weight: float
  viscera_weight: float
  shell_weight: float

@app.get("/")
def read_root():
  return {"message": "Welcome to the Abalone Age Prediction API!"}

@app.post("/predict")
async def predict(features: AbaloneFeatures):
  input_features = prepare_input(
      sex=features.sex,
      length=features.length,
      diameter=features.diameter,
      height=features.height,
      whole_weight=features.whole_weight,
      shucked_weight=features.shucked_weight,
      viscera_weight=features.viscera_weight,
      shell_weight=features.shell_weight
  )

  prediction = predict_age(input_features)

  return prediction
