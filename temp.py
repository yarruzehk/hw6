import json

import requests

from house.model import House

base_url = "http://localhost:8000"


def get_house_list() -> str:
    resp: requests.Response = requests.get(f"{base_url}/house/list")
    print(type(resp.text))  # -> string
    print(type(resp.json()))  # -> List[Dict]
    return resp.text


def work_with_json(input_str: str):
    with open("./data.json", "w") as fp:
        json.dump(json.loads(input_str), fp)


if __name__ == "__main__":
    data = get_house_list()
    work_with_json(data)
