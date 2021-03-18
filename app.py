# main application will go here
from typing import Optional

from fastapi import FastAPI

from house.endpoints import router as house_router
from student.endpoints import router as student_router
from users.endpoints import router

app = FastAPI()

app.include_router(router, prefix="/users")
app.include_router(house_router, prefix="/house")
app.include_router(student_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
