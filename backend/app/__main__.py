import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes import api

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(api.router)

if __name__ == "__main__":
    uvicorn.run("main:app")
