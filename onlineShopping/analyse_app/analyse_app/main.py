"""
Handles Analyse application
"""
from apis.customers import request
from configurations import *
import uvicorn
from fastapi import FastAPI

app = FastAPI()
request.entry_point(app)

uvicorn.run(app, host=app_host, port=app_port)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=app_port)