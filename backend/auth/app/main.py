# app/main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Message": "Hello from Praveen's Docker + FastAPI!"}