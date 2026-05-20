## 프로젝트 소개

## 프로젝트 폴더 구조

Youth_Social_Isolation_Risk_Predictor/
├─ data/
│  ├─ raw/
│  │  └─ youth_isolation.xlsx
│  └─ processed/
│     └─ isolation_selected.csv
├─ models/
│  └─ logistic_model.pkl
├─ notebooks/
├─ src/
│  ├─ youth_isolation/
│  │  ├─ __init__.py
│  │  ├─ config.py
│  │  ├─ preprocess.py
│  │  ├─ train_model.py
│  │  └─ predict.py
│  └─ app/
│     ├─ app.py
│     ├─ templates/
│     │  ├─ index.html
│     │  └─ result.html
│     └─ static/
│        └─ style.css
├─ .gitignore
├─ README.md
└─ requirements.txt

폴더 및 파일 설명
data/
프로젝트에 사용하는 데이터를 저장하는 폴더입니다.

data/raw/ : 원본 엑셀 데이터 저장
data/processed/ : 전처리 후 모델 학습에 사용할 데이터 저장
원본 데이터 파일은 다음 위치에 둡니다.

data/raw/youth_isolation.xlsx
전처리 결과는 다음 파일로 저장할 예정입니다.

data/processed/isolation_selected.csv
models/
학습이 끝난 머신러닝 모델을 저장하는 폴더입니다.

models/logistic_model.pkl
Flask 웹앱은 이 모델 파일을 불러와 사용자의 입력값에 대한 예측을 수행합니다.

notebooks/
데이터 확인, 전처리 실험, 모델 실험 등을 위한 Jupyter Notebook을 저장하는 폴더입니다.

실험용 코드는 이곳에 두고, 실제 실행용 코드는 src/ 폴더에 정리합니다.

src/youth_isolation/
머신러닝 관련 코드가 들어가는 폴더입니다.

config.py : 컬럼명, 파일 경로 등 프로젝트 설정 관리
preprocess.py : 원본 데이터 불러오기, 컬럼 선택, 결측치 제거, CSV 저장
train_model.py : 전처리 데이터로 로지스틱 회귀 모델 학습 및 저장
predict.py : 저장된 모델을 불러와 예측 결과와 위험도 반환
__init__.py : Python 패키지 인식용 파일
src/app/
Flask 웹앱 코드가 들어가는 폴더입니다.

app.py : Flask 서버 실행 및 라우팅 처리
templates/index.html : 사용자 입력 화면
templates/result.html : 예측 결과 화면
static/style.css : 웹 화면 스타일 파일
.gitignore
GitHub에 올리지 않을 파일을 정리하는 파일입니다.

예를 들어 가상환경, 캐시 파일, 원본 엑셀 데이터 등은 GitHub에 올리지 않습니다.

README.md
프로젝트 설명 문서입니다.

프로젝트 목적, 폴더 구조, 실행 방법, 모델 설명 등을 정리합니다.

requirements.txt
프로젝트 실행에 필요한 Python 패키지 목록입니다.

예시 패키지:

pandas
scikit-learn
flask
joblib
openpyxl
matplotlib
seaborn

## 사용 데이터

## 입력 변수

## 정답 라벨

## 모델 설명

## 실행 방법

`powershell`에
python src/app/app.py

또는
지금 쓰던 전체 경로 방식이면
& c:\Users\user\git\Youth_Social_Isolation_Risk_Predictor\.venv\Scripts\python.exe c:/Users/user/git/Youth_Social_Isolation_Risk_Predictor/src/app/app.py

http://127.0.0.1:5000
이런식으로 주소가 나오게 된다.
해당 주소를 url창에 넣고 엔터치면 된다.

## 결과 해석

## 한계점