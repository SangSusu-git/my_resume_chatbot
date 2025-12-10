import os
from dotenv import load_dotenv
load_dotenv(".env")
api_key = os.getenv("GOOGLE_API_KEY")
import base64

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage

class Gemini:
    def __init__(self, model_name = 'gemini-2.5-flash-lite'):
        # gemini-2.5-flash-lite
        # gemini-2.5-flash
        # 3.0 pro는 유료인듯
        self.llm = ChatGoogleGenerativeAI(model=model_name)
    
    def text_response(self, string):
        response = self.llm.stream(string)
        
        for chunk in response:
            print(chunk.text)
    
    def image_response(self, string, img='./합심기도 배경.png'):  
        with open(img, "rb") as img_file:
            img_data = base64.b64encode(img_file.read()).decode('utf-8')
        
        message = HumanMessage(
            content = [
                {"type": "text", "text": string},
                {
                    "type": "image",
                    "source_type": "base64",
                    "data": img_data,
                    "mime_type": "image/png",
                },
            ]
        )

        response = self.llm.stream([message])
        # response = self.llm.invoke([message])
        # print(response.content)
        for chunk in response:
            print(chunk.text)

