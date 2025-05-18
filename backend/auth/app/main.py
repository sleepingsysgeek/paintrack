# app/main.py
from fastapi import FastAPI
from auth.app.routes import router

app = FastAPI(title="Auth API", version="1.0.0")

app.include_router(router)