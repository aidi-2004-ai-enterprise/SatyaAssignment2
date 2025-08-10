# app/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import numpy as np
import joblib
import logging
import os

# Initialize FastAPI
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load model and encoder
try:
    model_bundle = joblib.load("app/data/model.joblib")
    model = model_bundle["model"]
    label_encoder = model_bundle["encoder"]
    logger.info("Model and encoder loaded successfully.")
except Exception as e:
    logger.error(f"Failed to load model: {e}")
    raise RuntimeError("Could not load model.")

# Pydantic input model
class PenguinFeatures(BaseModel):
    island: int = Field(..., description="Encoded island (0, 1, or 2)")
    bill_length_mm: float
    bill_depth_mm: float
    flipper_length_mm: float
    body_mass_g: float
    sex: int = Field(..., description="Encoded sex (0 or 1)")

@app.get("/")
def root():
    return {"message": "Penguin Species Classifier API is running."}

@app.post("/predict")
def predict_species(features: PenguinFeatures):
    try:
        # Convert input to 2D array for prediction
        input_data = np.array([
            [
                features.island,
                features.bill_length_mm,
                features.bill_depth_mm,
                features.flipper_length_mm,
                features.body_mass_g,
                features.sex
            ]
        ])

        # Make prediction
        prediction = model.predict(input_data)[0]

        # Decode predicted label
        predicted_species = label_encoder.inverse_transform([prediction])[0]

        return {"predicted_species": predicted_species}

    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        raise HTTPException(status_code=500, detail="Prediction failed.")
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
