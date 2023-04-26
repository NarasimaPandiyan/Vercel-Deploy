import os
from fastapi import FastAPI

app = FastAPI()

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("MONGO_URI")
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
    try:
        client.admin.command('ping')
        return {f"Pinged your deployment. You successfully connected to MongoDB! {db.list_collection_names()}"}
    except Exception as e:
        return({"error":e})

@app.get("/test/{chat}")
def hello(chat: str):
    return get_messages(chat) 

@app.get("/ping")
def hello():
    return {"ping":ping()}