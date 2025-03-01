from fastapi import FastAPI
import openai

import os
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()
openai.api_key = os.getenv("OPENAI_API")

@app.get("/chat")
def chat(query: str):
    response = openai.ChatCompletion.create(
        model="gpt-4", messages=[{"role": "user", "content": query}]
    )
    return {"response": response["choices"][0]["message"]["content"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
