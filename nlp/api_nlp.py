from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn


from fonctions import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/test")
def test():
    return "connection au main api fonctionnel"


@app.post("/text_to_text")
def ttt(text):
  
    return text_to_text(text)


@app.post("/text_to_speech")
def tts(text):
    return text_to_speech(text)

  
uvicorn.run(app,host="0.0.0.0", port=8000)
