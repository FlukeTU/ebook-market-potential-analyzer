import gradio as gr
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
# Dropdown choices
# -----------------------------
category_choices = [
    "Literature & Fiction",
    "Science Fiction & Fantasy",
    "Children's eBooks",
    "Biographies & Memoirs",
    "Law",
    "Business & Money",
    "Health, Fitness & Dieting",
    "Religion & Spirituality",
    "Romance",
    "Mystery, Thriller & Suspense",
    "Other"
]

seller_choices = [
    "Amazon.com Services LLC",
    "Random House LLC",
    "Penguin Group (USA) LLC",
    "HarperCollins Publishers",
    "Other Seller"
]

# -----------------------------
# Prediction function
# -----------------------------
def analyze_market_potential_final(
    stars,
    reviews,
    price,
    book_age_years,
    included_in_kindle_unlimited,
    published_date_not_available,
    category_grouped,
    soldby_grouped
):
    reviews = max(0, int(reviews))
    price = max(0.0, float(price))
    book_age_years = max(0.0, float(book_age_years))

    log_reviews = np.log1p(reviews)
    log_price = np.log1p(price)
    book_age_years_capped = min(book_age_years, 21.971253)

    input_df = pd.DataFrame([{
        "stars": stars,
        "log_reviews": log_reviews,
        "log_price": log_price,
        "book_age_years_capped": book_age_years_capped,
        "isKindleUnlimited": bool(included_in_kindle_unlimited),
        "publishedDate_missing": int(published_date_not_available),
        "category_grouped": category_grouped,
        "soldBy_grouped": soldby_grouped
    }])

    score = model.predict_proba(input_df)[:, 1][0]
    predicted_class = int(score >= THRESHOLD)

    if score >= 0.70:
        level = "High"
    elif score >= 0.40:
        level = "Moderate"
    else:
        level = "Low"

    prediction_result = "Likely Best Seller" if predicted_class == 1 else "Not Likely Best Seller"

    interpretation = f"""
Prediction Summary:
- Estimated bestseller score: {score:.4f}
- Decision threshold: {THRESHOLD:.2f}
- Prediction result: {prediction_result}
- Commercial potential level: {level}

Interpretation:
This result is generated from a Random Forest model trained on Amazon Kindle e-book data.
The app excludes badge-based variables to improve behavioral consistency and interpretability.
The score should be used as a decision-support signal for evaluating market potential, not as a guaranteed business outcome.
    """.strip()

    return (
        round(float(score), 4),
        prediction_result,
        level,
        interpretation
    )

# -----------------------------
# Build app
# -----------------------------
with gr.Blocks(title="E-Book Market Potential Analyzer") as demo:
    gr.Markdown(f"""
    # E-Book Market Potential Analyzer
    This prototype evaluates the potential market performance of an e-book on an online platform using a machine learning model.

    **Final Model:** Random Forest (No Badge)  
    **Decision Threshold:** {THRESHOLD:.2f}
    """)

    with gr.Row():
        with gr.Column():
            stars = gr.Slider(
                minimum=0.0,
                maximum=5.0,
                value=4.5,
                step=0.1,
                label="Star Rating"
            )

            reviews = gr.Number(
                value=100,
                precision=0,
                label="Number of Reviews"
            )

            price = gr.Number(
                value=9.99,
                label="Price"
            )

            book_age_years = gr.Number(
                value=3.0,
                label="Book Age (Years)"
            )

            included_in_kindle_unlimited = gr.Checkbox(
                value=False,
                label="Included in Kindle Unlimited"
            )

            published_date_not_available = gr.Checkbox(
                value=False,
                label="Published Date Not Available"
            )

            category_grouped = gr.Dropdown(
                choices=category_choices,
                value="Literature & Fiction",
                label="Book Category"
            )

            soldby_grouped = gr.Dropdown(
                choices=seller_choices,
                value="Amazon.com Services LLC",
                label="Sold By"
            )

            analyze_btn = gr.Button("Analyze Market Potential")

        with gr.Column():
            output_score = gr.Number(label="Estimated Bestseller Score")
            output_prediction = gr.Textbox(label="Prediction Result")
            output_level = gr.Textbox(label="Commercial Potential Level")
            output_interpretation = gr.Textbox(label="Model Interpretation", lines=10)

    analyze_btn.click(
        fn=analyze_market_potential_final,
        inputs=[
            stars,
            reviews,
            price,
            book_age_years,
            included_in_kindle_unlimited,
            published_date_not_available,
            category_grouped,
            soldby_grouped
        ],
        outputs=[
            output_score,
            output_prediction,
            output_level,
            output_interpretation
        ]
    )

demo.launch()