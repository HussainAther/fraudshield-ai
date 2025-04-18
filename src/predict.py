import xgboost as xgb
import mlflow
import mlflow.xgboost
import pandas as pd

# Load model from MLflow
model_uri = "models:/fraud_detector/1"  # Replace version if needed
model = mlflow.xgboost.load_model(model_uri)

def predict_transaction(data: dict) -> dict:
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    proba = model.predict_proba(df)[0][1]
    return {
        "fraud_probability": round(float(proba), 4),
        "is_fraud": bool(prediction)
    }

