from typing import List

from fastapi import APIRouter, HTTPException

from house.model import House

router = APIRouter()

houses = [House(["bill"], "purple")]


@router.get("/create")
def create_ep(color: str):
    h = House(["john"], color)
    houses.append(h)

    return h


@router.get("/update_try_catch")
def update_ep(index: int, employee: str, new_color: str = None, method: str = "add"):
    try:
        if new_color is not None:
            houses[index].color = new_color
        if method == "add":
            houses[index].employees.append(employee)

    except Exception:
        return "there was an issue"


@router.get("/update")
def update1_ep(index: int, employee: str, new_color: str = None, method: str = "add"):
    if index > len(houses):
        raise HTTPException(422, "index out of range")
    h = houses[index]
    h.color = new_color or h.color
    if method == "add":
        h.employees.append(employee)
    return h


@router.get("/list")
def list_ep():
    ret = []
    for i, h in enumerate(houses):
        ret.append(
            {"id": id(h), "index": i, "house": h, "square_footage": h.square_footage()}
        )
    return ret
