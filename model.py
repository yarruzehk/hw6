from pydantic import BaseModel


class Student(BaseModel):
    file: str = "./student.json"

    first_name: str
    last_name: str


if __name__ == "__main__":
    import json

    s1 = Student(first_name="z", last_name="z")
    x = 1
    with open(s1.file, "w") as fp:
        json.dump(s1.json(), fp)
