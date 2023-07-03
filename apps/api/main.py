from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from langchain.llms import OpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

app = FastAPI()


@app.get("/api/healthchecker")
def healthchecker():
    return {"status": "success", "message": "Integrate FastAPI Framework with Next.js"}


@app.post("/api/v1/chat")
def chat():
  llm = OpenAI(streaming=True, callbacks=[StreamingStdOutCallbackHandler()], temperature=0)
  resp = llm("Write me a song about sparkling water.")
  
  llm.generate(["Tell me a joke."])
  return {"status": "success", "message": "chat api endpoint"}


