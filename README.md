# 💸 FraudShield AI

An AI-powered web app for detecting potentially fraudulent financial transactions in real-time, built using HP AI Studio, MLflow, and XGBoost.

This project is submitted for the **HP & NVIDIA Developer Challenge 2025** and demonstrates the use of local AI development tools to solve real-world financial industry challenges through secure, scalable AI deployment.

---

## 🧠 Project Summary

**FraudShield AI** uses an XGBoost model trained on anonymized credit card transaction data to identify patterns that indicate potential fraud. The app exposes a simple API via Swagger and supports integration with existing transaction pipelines.

- **Industry**: Finance
- **Category**: Enterprise Data Analysis
- **Use Case**: Fraud prevention
- **Tech Stack**: Python, XGBoost, MLflow, Flask, HP AI Studio

---

## 🚀 Features

- Real-time fraud detection API
- Trained on Kaggle credit card dataset
- Integrated with MLflow for tracking models, metrics, and artifacts
- Deployed via Swagger using HP AI Studio
- Extensible pipeline with `requirements.txt` support for reproducibility

---

## 📊 Input Format

The model expects a JSON input representing one transaction:

```json
{
  "Amount": 149.62,
  "V1": -1.359807,
  "V2": -0.072781,
  ...
  "V28": 0.239599
}
```

---

## 🔧 Getting Started (Locally or via HP AI Studio)

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/fraudshield-ai.git
cd fraudshield-ai
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Train the Model & Track with MLflow
```bash
python src/train_model.py
```

### 4. Run the API
```bash
python demo/app.py
```

Swagger UI will be available at:  
**`http://localhost:5000/docs`**

---

## 💻 Project Structure

```
fraudshield-ai/
├── data/                   # Dataset storage
├── notebooks/              # Experimentation notebooks
├── src/                    # Core logic
│   ├── train_model.py      # Training and MLflow logging
│   ├── predict.py          # Prediction logic
│   └── utils.py            # Helper functions
├── demo/                   # Swagger API + demo artifacts
│   ├── app.py              # Flask app for inference
│   └── example_input.json  # Sample Swagger input
├── requirements.txt
├── README.md
└── mlruns/                 # MLflow runs (auto-generated)
```

---

## 📈 Model Performance

| Metric | Score |
|--------|-------|
| AUC    | 0.992 |
| Accuracy | ~99.7% (on imbalanced dataset) |

*Note: We used undersampling and class weighting to improve detection of rare fraudulent cases.*

---

## 📬 Submission Notes

- ML model trained and logged with MLflow inside HP AI Studio
- Model deployed via Swagger for RESTful access
- FraudShield AI meets requirements of local, on-prem AI development
- Includes demo folder for automatic deployment in HP AI Studio

---

## 🛠 Tools Used

- **HP AI Studio** – Secure, containerized local development
- **MLflow** – Model tracking and versioning
- **XGBoost** – Gradient boosting for fraud detection
- **Flask** – Lightweight API server
- **Swagger** – Auto-generated documentation for endpoint testing

---

## 💬 Contact

Have questions or want to collaborate?  
Drop a message on [Discord](https://discord.gg/devpost) or reach me via Devpost: **@HussainAther**

---

© 2025 FraudShield AI • Made with ❤️ for HP & NVIDIA Developer Challenge
