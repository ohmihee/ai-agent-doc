import os
from openai import OpenAI
from dotenv import load_dotenv

# .env 파일의 환경 변수 로드
load_dotenv()

def get_openai_client():
    """_
    OpenAI 클라이언트를 생성하여 반환합니다.
    API  키가 없을 경우 시스템을 즉시 종료
    """
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        raise ValueError("환경 변수 'OPENAI_API_KEY'가 설정되지 않았습니다. .env 파일을 확인하세요 ")
    
    return OpenAI(api_key=api_key)


openai_client = get_openai_client()    