import os
from fastapi import FastAPI
from mongoDB import ping, get_messages, post_message

app = FastAPI()

@app.get("/test/{chat}")
def hello(chat: str):
    return get_messages(chat) 

@app.get("/ping")
def hello():
    return {"ping":ping()}