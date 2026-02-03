from core.client import openai_client

def generate_summary(text):
    try:
        response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role":"system", "content":"너는 요약 전문가야"},
                {"role":"user", "content":f"다음 내용을 요약해줘: {text}"}
                # {"role":"user", "content":"1+1은?"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"API 호출 중 오류 발생: {e}")
        return None