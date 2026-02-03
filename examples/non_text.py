from core.client import openai_client

def encode_image_from_url(url):
    """URL의 이미지를 다운로드하여 Base64로 변환"""

def analyze_image_url():
    try:
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
                            "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/3b/LeBron_James_Layup_%28Cleveland_vs_Brooklyn_2018%29.jpg"
                        }
                    ]
                }
            ]
        )
        
        print(response.output_text)
    
    except Exception as e:
        print(f"API 호출 중 오류 발생: {e}")
        return None
    
    
