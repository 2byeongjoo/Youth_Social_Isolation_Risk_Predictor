# 모듈 및 라이브러리 임포트
import pandas as pd

## 엑셀 파일로부터 데이터 불러오기, 데이터프레임 생성, 데이터 확인

# 원본 데이터가 담겨있는 엑셀 파일 불러오기
df = pd.read_excel("data/raw/youth_isolation.xlsx", sheet_name="Data")

# 필요한 컬럼만 추출
selected_columns = ["A7", "A10", "A11", "A13_1", "A13_3", "A13_4", "A17", "A18_1", "A18_3", "B1_2", "KEY_1"]

# 선택한 컬럼으로 전처리용 데이터프레임 생성
data = df[selected_columns].copy()

# 데이터 확인(상위 5개 데이터, 결측치 확인, "KEY_1" 데이터 값의 전체 갯수)
print("상위 5개 데이터 확인:\n",data.head())
print()
print(f"각 컬럼 별 결측치의 갯수:\n{data.isnull().sum()}")
print()
print("KEY_1의 값의 갯수:\n",data["KEY_1"].value_counts())
print()

## 데이터 전처리 후 .csv 파일로 저장

# 결측치 제거 전 데이터 크기 확인
print("결측치 제거 전 데이터 크기:", data.shape)
print()

# 결측치 제거
data_clean = data.dropna().copy()

# 결측치 제거 후 데이터 크기 확인
print("결측치 제거 후 데이터 크기:", data_clean.shape)
print()

# 라벨 분포 확인
print("라벨 개수:\n",data_clean["KEY_1"].value_counts())
print()

print("라벨 비율:\n",data_clean["KEY_1"].value_counts(normalize=True))
print()

# 최종 .csv파일로 저장하기.
data_clean.to_csv("data/processed/isolation_selected.csv", index=False, encoding="utf-8-sig")