### python 가상환경 구축
python -m venv .venv

### 활성화 
#### window
.venv/Scripts/activate

#### mac
source .venv/bin/activate

#### 비활성화
deactivate

### 의존성 관리
pip freeze > requirements.txt
pip install -r requirements.txt

pip install openai
pip install python-dotenv


####
pip : 파이썬에서 패키지를 설치하고 관리하는 패키지 인스톨러
- 파이썬 가상환경 구축 후 해당 환경 활성화 후 패키지 설치 시에는 .venu 하위의 lib 폴더 안에 생성된다.

#### Extension
- autoDocstring
    파이썬 코드에서 함수와 클래스에 필요한 docstring을 자동으로 생성해줌
    사용법 : 함수나 클래스 위에서 """ 입력 후 tab 클릭
