# main application will go here
from fastapi import FastAPI

from house.endpoints import router as house_router
from users.endpoints import router

app = FastAPI()

app.include_router(router, prefix="/users")
app.include_router(house_router, prefix="/house")
