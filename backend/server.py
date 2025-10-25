from fastapi import FastAPI
import uvicorn
from base_agent import Agent

app = FastAPI()
agent = Agent()

@app.get("/")
async def chat(prompt):
    return agent.chat(prompt)
    
if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000)