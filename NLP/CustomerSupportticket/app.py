
import json
from pathlib import Path

import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware

# --------------------------------------------------
# 1. Configure paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
ARTIFACTS_DIR = BASE_DIR / "notesbook" / "artifacts"

MODEL_PATH = ARTIFACTS_DIR / "banking77_intent_pipeline.joblib"
LABELS_PATH = ARTIFACTS_DIR / "banking77_labels.json"


# --------------------------------------------------
# 2. Load the trained model and intent labels
# --------------------------------------------------

if not MODEL_PATH.exists():
    raise FileNotFoundError(
        f"Model file not found: {MODEL_PATH}"
    )

if not LABELS_PATH.exists():
    raise FileNotFoundError(
        f"Intent labels file not found: {LABELS_PATH}"
    )

model = joblib.load(MODEL_PATH)

with open(LABELS_PATH, "r", encoding="utf-8") as file:
    label_records = json.load(file)

id_to_intent = {
    item["label"]: item["intent"]
    for item in label_records
}


# --------------------------------------------------
# 3. Create FastAPI application
# --------------------------------------------------

app = FastAPI(
    title="Banking77 Intent Classification API",
    description=(
        "Predict the intent behind a "
        "customer-support message."
    ),
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# 4. Define request schema
# --------------------------------------------------

class PredictionRequest(BaseModel):
    text: str = Field(
        min_length=1,
        max_length=2000,
        description="Customer-support message"
    )


# --------------------------------------------------
# 5. Home endpoint
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "Banking77 Intent Classification API is running",
        "status": "healthy"
    }


# --------------------------------------------------
# 6. Prediction endpoint
# --------------------------------------------------

@app.post("/predict")
def predict(request: PredictionRequest):
    message = request.text.strip()

    if not message:
        raise HTTPException(
            status_code=422,
            detail="Please enter a non-empty message."
        )

    predicted_label = int(model.predict([message])[0])

    predicted_intent = id_to_intent.get(predicted_label)

    if predicted_intent is None:
        raise HTTPException(
            status_code=500,
            detail="Predicted label has no matching intent."
        )

    return {
        "input_text": message,
        "predicted_label": predicted_label,
        "predicted_intent": predicted_intent
    }
