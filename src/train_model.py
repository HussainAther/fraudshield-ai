import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
import mlflow
import mlflow.xgboost
import os

# Load dataset
df = pd.read_csv("data/creditcard.csv")
X = df.drop("Class", axis=1)
y = df["Class"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.3, random_state=42)

# Enable MLflow autologging
mlflow.xgboost.autolog()

with mlflow.start_run():
    model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss', scale_pos_weight=100)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    auc = roc_auc_score(y_test, preds)

    print("Classification Report:")
    print(classification_report(y_test, preds))
    print("AUC:", auc)

