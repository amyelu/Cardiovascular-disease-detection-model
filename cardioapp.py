from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load trained model
model = joblib.load("Cardiovascular_detection_model.pkl")

# Initialize FastAPI app
app = FastAPI()

# Define request body format
class FeaturesInput(BaseModel):
    features: list[float]

@app.get("/")
def home():
    return {"message": "Cardiovascular Disease Prediction API"}

@app.post("/predict")
def predict(data: FeaturesInput):
    try:
        features = np.array(data.features).reshape(1, -1)

        # Get probability of class 1 (cardiovascular disease)
        prediction_prob = model.predict_proba(features)[0][1]

        # Convert probability into human-readable labels
        if prediction_prob > 0.7:
            result = "High chance of Cardiovascular disease"
        elif prediction_prob > 0.4:
            result = "Moderate chance of Cardiovascular disease"
        else:
            result = "Low chance of Cardiovascular disease"

        return {"prediction": result, "probability": float(prediction_prob)}

    except Exception as e:
        return {"error": str(e)}

