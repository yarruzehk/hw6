# main application will go here
from fastapi import FastAPI
from users.endpoints import router

app = FastAPI()

app.include_router(router, prefix="/users")
