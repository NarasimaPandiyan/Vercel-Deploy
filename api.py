import os
from fastapi import FastAPI

app = FastAPI()

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

uri ='mongodb+srv://Narasima:OHgveZ8HKHPx1vYv@test.zwpiuqo.mongodb.net/?retryWrites=true&w=majority'
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.CalmCove

def post_message(chat: str, message: str):
    pass

def get_messages(chat: str):
    cursor = db[chat].find({},{'_id': False})
    data = []
    for doc in cursor:
        data.append(doc)
    return data

def ping():
    return db.list_collection_names()

@app.get("/test/{chat}")
def hello(chat: str):
    return get_messages(chat) 

@app.get("/ping")
def hello():
    return {"ping": db.list_collection_names()}