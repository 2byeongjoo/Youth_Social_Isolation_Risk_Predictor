import sys
from pathlib import Path

from flask import Flask, render_template, request

# src 폴더를 import 경로에 추가
BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

from youth_isolation.predict import predict_isolation


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    input_data = {
        "A7": int(request.form["A7"]),
        "A10": float(request.form["A10"]),
        "A11": float(request.form["A11"]),
        "A13_1": int(request.form["A13_1"]),
        "A13_3": int(request.form["A13_3"]),
        "A13_4": int(request.form["A13_4"]),
        "A17": int(request.form["A17"]),
        "A18_1": int(request.form["A18_1"]),
        "A18_3": int(request.form["A18_3"]),
        "B1_2": int(request.form["B1_2"]),
    }

    result = predict_isolation(input_data)

    probability_percent = round(result["isolation_probability"] * 100, 1)

    return render_template(
        "result.html",
        prediction=result["prediction"],
        prediction_label=result["prediction_label"],
        probability_percent=probability_percent,
    )


if __name__ == "__main__":
    app.run(debug=True)