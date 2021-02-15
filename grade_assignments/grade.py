import os

from git import Repo
from settings import config
from pathlib import Path
from shutil import copy, rmtree
import pandas as pd

from util import snake_case, count_passing_tests


def load_sheet(sheet_name: str = config.sheet):
    p = Path(sheet_name)
    df: pd.DataFrame = pd.ExcelFile(p.absolute()).parse()
    for row in df.iterrows():
        yield row


def clean_dict(row, assignment: str):
    d = {snake_case(k): v for k, v in dict(row[1]).items()}
    d["username"] = d["school_email"].split("@")[0].lower()
    d["assignment"] = assignment
    d["homework"] = None if d.get("homework", "nan") == "nan" else d["homework"]
    return d


def make_repo_dir(username: str, assignment: str, **kwargs):
    p = Path(f"../../assignments/{assignment}/{username}/")
    rmtree(p)
    p.mkdir(parents=True, exist_ok=True)
    return p


if __name__ == "__main__":
    from pprint import pprint

    assignment = "hw2"
    local_test_dir = ".."
    local_test_file = "test/test_hw2.py"
    ret = []
    for idx, row in enumerate(load_sheet()):
        info = clean_dict(row, assignment)
        info["row"] = idx
        if not info:
            continue
        d = make_repo_dir(**info)
        print(info["username"], info["homework"])
        if hw := info.get("homework"):
            if isinstance(hw, float):
                info["grade"] = 0
                continue
            try:
                if len(os.listdir(f"{d.absolute()}")):
                    r: Repo = Repo(d.absolute())
                else:
                    r: Repo = Repo.clone_from(hw, d.absolute(), env={})
            except Exception:
                continue
            test_dir = d / local_test_file
            if not test_dir.parent.is_dir():
                test_dir.parent.mkdir()
            hw_file = d / "homework/hw2.py"
            if not hw_file.is_file():
                info["grade"] = 0
                continue
            copy(f"{local_test_dir}/{local_test_file}", test_dir)
            q = os.popen(f"pytest -- {test_dir.absolute()}").read()
            info["grade"] = count_passing_tests(q) / 20
            x = 1
            ret.append(info)
            continue
        info["grade"] = 0
        info["row"] = idx
    pprint([(d["row"], d["username"], d["grade"]) for d in ret])
