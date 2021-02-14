from typing import Any, List


def first(a: List[Any], cmd: str):
    cmd = cmd.strip().lower()
    if not a or cmd not in ["start", "first", "end"]:
        return None
    if cmd == "end":
        return next(reversed(a))
    return next(iter(a))
