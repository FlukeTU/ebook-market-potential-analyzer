from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
import joblib
import json

# -----------------------------
# Load model and metadata
# -----------------------------
MODEL_PATH = "model_artifacts/final_rf_no_badge_pipeline.joblib"
METADATA_PATH = "model_artifacts/final_app_metadata.json"

model = joblib.load(MODEL_PATH)

with open(METADATA_PATH, "r", encoding="utf-8") as f:
    metadata = json.load(f)

THRESHOLD = 0.60

# -----------------------------
# FastAPI app
# -----------------------------
app = FastAPI(title="E-Book Market Potential API")

# -----------------------------
# Input schema
# -----------------------------
class PredictionInput(BaseModel):
    stars: float
    reviews: int
    price: float
    book_age_years: float
    included_in_kindle_unlimited: bool
    published_date_not_available: bool
    category_grouped: str
    soldby_grouped: str

# -----------------------------
# Health check
# -----------------------------
@app.get("/")
def root():
    return {
        "message": "E-Book Market Potential API is running",
        "model": "Random Forest (No Badge)",
        "threshold": THRESHOLD
    }

# -----------------------------
# Prediction endpoint
# -----------------------------
@app.post("/predict")
def predict(payload: PredictionInput):
    reviews = max(0, int(payload.reviews))
    price = max(0.0, float(payload.price))
    book_age_years = max(0.0, float(payload.book_age_years))

    log_reviews = np.log1p(reviews)
    log_price = np.log1p(price)
    book_age_years_capped = min(book_age_years, 21.971253)

    input_df = pd.DataFrame([{
        "stars": payload.stars,
        "log_reviews": log_reviews,
        "log_price": log_price,
        "book_age_years_capped": book_age_years_capped,
        "isKindleUnlimited": bool(payload.included_in_kindle_unlimited),
        "publishedDate_missing": int(payload.published_date_not_available),
        "category_grouped": payload.category_grouped,
        "soldBy_grouped": payload.soldby_grouped
    }])

    score = float(model.predict_proba(input_df)[:, 1][0])
    predicted_class = int(score >= THRESHOLD)

    if score >= 0.70:
        level = "High"
    elif score >= 0.40:
        level = "Moderate"
    else:
        level = "Low"

    prediction_result = "Likely Best Seller" if predicted_class == 1 else "Not Likely Best Seller"

    return {
        "estimated_bestseller_score": round(score, 4),
        "prediction_result": prediction_result,
        "commercial_potential_level": level,
        "decision_threshold": THRESHOLD,
        "model_name": "Random Forest (No Badge)"
    }