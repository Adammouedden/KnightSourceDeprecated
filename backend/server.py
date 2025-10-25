from fastapi import FastAPI
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
gemini_key = os.getenv("GEMINI_API")
client = genai.Client(gemini_key)

app = FastAPI()

@app.get("/")
async def chat(prompt):
    return call_gemini(prompt)
    

def call_gemini(prompt):
    return client.models.generate_content(model='gemini-2.5-flash', content=prompt)
