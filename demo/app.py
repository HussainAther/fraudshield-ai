from flask import Flask, request, jsonify
from src.predict import predict_transaction

app = Flask(__name__)

@app.route("/")
def home():
    return "FraudShield AI is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        result = predict_transaction(data)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

