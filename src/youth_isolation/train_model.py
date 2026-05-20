# 모듈 및 라이브러리 임포트
import pandas as pd
# 로지스틱 회귀 및 혼동행렬
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# 전처리된 CSV 파일 다시 불러오기
model_data = pd.read_csv("data/processed/isolation_selected.csv")

## 입력값 X, 정답 y 분리
X = model_data[["A7", "A10", "A11", "A13_1", "A13_3", "A13_4", "A17", "A18_1", "A18_3", "B1_2"]]
y = model_data["KEY_1"]

# 학습/테스트 분리
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 로지스틱 회귀 모델
model = LogisticRegression(max_iter=1000, class_weight="balanced")
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)

# 평가
print("정확도:", accuracy_score(y_test, y_pred))
print("혼동행렬:")
print(confusion_matrix(y_test, y_pred))
print("분류 리포트:")
print(classification_report(y_test, y_pred))

# 한글 폰트 설정
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# 실제 라벨과 예측 라벨 분포 비교 시각화
actual_counts = pd.Series(y_test).value_counts().reindex([1, 2], fill_value=0)
pred_counts = pd.Series(y_pred).value_counts().reindex([1, 2], fill_value=0)

label_names = ["고립은둔", "미해당"]

x = range(len(label_names))
bar_width = 0.35

plt.figure(figsize=(6, 5))

plt.bar(
    [i - bar_width / 2 for i in x],
    actual_counts,
    width=bar_width,
    label="실제값"
)

plt.bar(
    [i + bar_width / 2 for i in x],
    pred_counts,
    width=bar_width,
    label="예측값"
)

plt.xticks(x, label_names)
plt.xlabel("분류")
plt.ylabel("개수")
plt.title("실제값과 예측값 분포 비교")
plt.legend()
plt.tight_layout()
plt.savefig("reports/figures/classification_distribution.png", dpi=300)
plt.close()

# 혼동행렬 시각화
cm = confusion_matrix(y_test, y_pred, labels=[1, 2]) # 고립운동, 미해당 순으로 고정

plt.figure(figsize=(6, 5))
ax = sns.heatmap(
    cm,
    annot=True, # 각 칸에 숫자 직접 표시 지정하는 옵션
    fmt="d",  # 정수형 포맷
    cmap="Blues", # 팔레트 색깔 파란색
    xticklabels=["고립은둔", "미해당"], # x눈금 라벨
    yticklabels=["고립은둔", "미해당"]  # y눈금 라벨
)

ax.xaxis.tick_top() # 눈금 라벨 위쪽으로
ax.xaxis.set_label_position("top") # 제목 라벨 위쪽으로

plt.xlabel("예측값")
plt.ylabel("실제값")
plt.title("사회적 고립 예측 모델의 혼동행렬", pad=40) # 표 제목 패딩값 : 40
plt.tight_layout() # 그래프 요소들이 서로 겹치지 않도록 자동 여백 코드
plt.savefig("reports/figures/confusion_matrix.png", dpi=300) # dpi 해상도, 높을수록 이미지 선명해짐.
plt.close()

joblib.dump(model, "models/logistic_model.pkl")
print("모델 저장 완료: models/logistic_model.pkl")