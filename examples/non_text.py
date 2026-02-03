from core.client import openai_client
import base64
import requests

def encode_image_from_url(url: str):
    """URL의 이미지를 다운로드하여 Base64로 변환"""
    response = requests.get(url)
    if response.status_code == 200:
        return base64.b64decode(response.content).decode('utf-8')
    else:
        raise Exception(f"이미지 다운로드 실패. 상태 코드: {response.status_code}")
    # API 호출 중 오류 발생 : 이미지 다운로드 실패, 상태 코드 403 Forbidden
    # 위 에러의 경우 위키미디어가 "브라우저가 아닌 자동화된 프로그램 (봇)이구나?, 접근을 허용하지 않겠어" 하고 접근 하지 못하도록 하여 발생한 에러이다.

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
    
    
