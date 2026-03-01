from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.efficientnet import preprocess_input
from werkzeug.utils import secure_filename
from PIL import Image
import numpy as np
import os
import secrets

app = Flask(__name__)
app.secret_key = "supersecretkey"

UPLOAD_FOLDER = "uploads"
STATIC_FOLDER = "static"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(os.path.join(STATIC_FOLDER, "images"), exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["STATIC_FOLDER"] = STATIC_FOLDER

# Load model
model = load_model("plantcare_efficientnet_model.keras")

# Class labels (IMPORTANT: must match training order)
import json

with open("class_indices.json", "r") as f:
    class_indices = json.load(f)

class_labels = list(class_indices.keys())


def predict_image(img_path):
    img = Image.open(img_path).convert("RGB")
    img = img.resize((160, 160))

    img_array = np.array(img)
    img_array = preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)

    predicted_index = np.argmax(prediction, axis=1)[0]
    confidence = float(np.max(prediction)) * 100

    predicted_class = class_labels[predicted_index]

    return predicted_class, round(confidence, 2)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/upload")
def upload():
    return render_template("upload.html")


@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)

    prediction, confidence = predict_image(filepath)
    session["confidence"] = confidence

    static_filename = f"upload_{secrets.token_hex(8)}.jpg"
    static_path = os.path.join(app.config["STATIC_FOLDER"], "images", static_filename)
    Image.open(filepath).save(static_path)

    session["prediction"] = prediction
    session["image_path"] = f"images/{static_filename}"

    os.remove(filepath)

    return jsonify({"success": True})


@app.route("/result")
def result():
    prediction = session.get("prediction")
    image_path = session.get("image_path")

    if not prediction:
        return redirect(url_for("upload"))

    confidence = session.get("confidence")

    return render_template(
        "result.html",
        prediction=prediction,
        image_path=image_path,
        confidence=confidence
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)