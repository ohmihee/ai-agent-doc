from core.client import openai_client
import base64
import requests

def encode_image_from_url(url: str):
    """URL의 이미지를 다운로드하여 Base64로 변환"""
    # 1. 403(Forbidden) 문제 해결을 위해 headers 추가
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # 2. 이미지 바이너리 → base64.b64encode(base64 바이너리) → .decode(’utf-8’)(base64 문자열) 변환
        return base64.b64encode(response.content).decode('utf-8')
    else:
        raise Exception(f"이미지 다운로드 실패. 상태 코드: {response.status_code}")
    # API 호출 중 오류 발생 : 
    # 1. 이미지 다운로드 실패, 상태 코드 403 Forbidden
    # 위 에러의 경우 위키미디어가 "브라우저가 아닌 자동화된 프로그램 (봇)이구나?, 접근을 허용하지 않겠어" 하고 접근 하지 못하도록 하여 발생한 에러이다.
    # 2.'utf-8' codec can't decode byte 0xb4 in position 3: invalid start byte
    # 이미지의 바이너리(이진) 데이터를 강제로 **텍스트(UTF-8)**로 해석하려고 할 때 발생하는 파이썬 인코딩 오류이다. 이미지는 글자가 아닌 데이터 덩어리이기 때문에 decode(’utf-8’)을 바로 적용하기 어렵다.

def analyze_image_url(image_url: str):
    """_summary_
    Args:
        image_url (str): _description_
    Returns:
        _type_: _description_
    """
    try:
        # 이미지를 base64로 변환
        base64_image = encode_image_from_url(image_url)    
        
        response = openai_client.responses.create(
            model="gpt-5",
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": "What teams are playing in this image?",
                        },
                        {
                            "type": "input_image",
                            "image_url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    ]
                }
            ]
        )
        
        print(response.output_text)
    
    except Exception as e:
        print(f"API 호출 중 오류 발생: {e}")
        return None
    
    
