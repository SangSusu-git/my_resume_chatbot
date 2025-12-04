import os
from dotenv import load_dotenv
load_dotenv(".env")
api_key = os.getenv("GOOGLE_API_KEY")

from langchain_google_genai import ChatGoogleGenerativeAI

# 특정 구성으로 Gemini 모델 초기화
# gemini-2.5-flash-lite
# gemini-2.5-flash
llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite', temperature=0.9)

# 모델에 프롬프트를 보내고 응답 받기
response = llm.stream('langchain_google_genai에서 ChatGoogleGenerativeAI 함수의 역할을 설명해주세요.')
# print(response)
for chunk in response:
    print(chunk.text)
