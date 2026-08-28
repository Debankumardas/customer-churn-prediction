from pathlib import Path

import joblib
import pandas as pd


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Path to saved model
MODEL_PATH = BASE_DIR / "models" / "churn_model.joblib"


# Load saved model package
model_package = joblib.load(MODEL_PATH)

model = model_package["model"]
preprocessor = model_package["preprocessor"]
threshold = model_package["threshold"]


def predict_churn(customer_data):
    """
    Predict customer churn.

    Parameters
    ----------
    customer_data : dict
        Customer information.

    Returns
    -------
    dict
        Churn probability, prediction, and risk level.
    """

    # Convert dictionary to DataFrame
    data = pd.DataFrame([customer_data])

    # Remove customerID if provided
    if "customerID" in data.columns:
        data = data.drop(columns=["customerID"])

    # Ensure TotalCharges is numeric
    if "TotalCharges" in data.columns:
        data["TotalCharges"] = pd.to_numeric(
            data["TotalCharges"],
            errors="coerce"
        )

    # Apply saved preprocessing
    processed_data = preprocessor.transform(data)

    # Calculate churn probability
    churn_probability = model.predict_proba(
        processed_data
    )[0, 1]

    # Apply optimized threshold
    prediction = int(churn_probability >= threshold)

    # Determine risk level
    if churn_probability >= 0.60:
        risk_level = "High"
    elif churn_probability >= threshold:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    return {
        "churn_probability": round(float(churn_probability), 4),
        "prediction": prediction,
        "risk_level": risk_level
    }