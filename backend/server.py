from fastapi import FastAPI
from google import genai
from dotenv import load_dotenv
import os
import uvicorn

load_dotenv()
gemini_key = os.getenv("GEMINI_API")
client = genai.Client(api_key=gemini_key)

app = FastAPI()

@app.get("/")
async def chat(prompt):
    return call_gemini(prompt)
    

def call_gemini(prompt):
    response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
    return response.text

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000)