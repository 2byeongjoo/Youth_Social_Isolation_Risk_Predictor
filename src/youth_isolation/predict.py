import joblib
import pandas as pd


# 모델 파일 경로
model_path = "models/logistic_model.pkl"

# 입력 컬럼
feature_columns = [
    "A7",
    "A10",
    "A11",
    "A13_1",
    "A13_3",
    "A13_4",
    "A17",
    "A18_1",
    "A18_3",
    "B1_2",
]


# 모델 불러오기
model = joblib.load(model_path)


def predict_isolation(input_data):
    input_df = pd.DataFrame([input_data], columns=feature_columns)

    prediction = model.predict(input_df)[0]
    probabilities = model.predict_proba(input_df)[0]

    class_index = list(model.classes_).index(1)
    isolation_probability = probabilities[class_index]

    if prediction == 1:
        prediction_label = "고립은둔 청년"
    else:
        prediction_label = "미해당"

    return {
        "prediction": int(prediction),
        "prediction_label": prediction_label,
        "isolation_probability": isolation_probability,
    }