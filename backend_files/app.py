
from flask import Flask, request, jsonify
import pandas as pd
import joblib
import io 
import os

#Initalize Flask
superkart_api = Flask(___name___)

#load the trained model and preprocessing
model_path = os.path.join(
  os.pathdirnam(___file__),
  "superkart_model.joblib"
  )
model = joblib.load(model_path)

#Check whether the API is running
@superkart_api.get("/")
def home():
  return jsonify({"message": "SuperKart API is running"})

#Predict sales for a single product
@superkart_api.post("/v1/predict")
def predict():
  try:
    data = request.get_json()
    if not isinstance(data, dict):
      return jsonify({"error": "Expected a JSON object"}), 400

      input_df = pd.DataFrame([data])
      prediction = model.predict(input_df)

      return jsonify({
      "predicted_sales": float(prediction[0])

      })
      except Exception as e:
      return jsonify({"error": str(e)}), 400
#Predict sales for multiple products@superkart_api.post("/v1/predictbatch")
def predict_batch():
  try:
    if "file" not in request.files:
      return jsonify({"error": "CSV file required"}), 400

    file = request.files["file"]
    batch_df = pd.read_csv(file)

    predictions = model.predict(batch_df)

    return jsonify({
      "predictions": predictions.tollist()
      })
      except Exception as e:
      return jsonify({"error": str(e)}), 400
# Start the Flask application
if __name__ == "__main__":
  superkart_api.run(host="0.0.0.0", port=7860)
