from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    
    if not data or "text" not in data or not data["text"].strip():
        return jsonify({"error": "Please provide a job description"}), 400

    text = data["text"]
    vector = vectorizer.transform([text])
    prediction = model.predict(vector)[0]
    probability = model.predict_proba(vector)[0].max()

    result = "Fake" if prediction == 1 else "Legitimate"

    return jsonify({
        "prediction": result,
        "confidence": round(float(probability * 100), 2)
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)