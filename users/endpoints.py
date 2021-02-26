from fastapi import APIRouter

router = APIRouter()


@router.get("/users")
def get_users_endpoint(name: str):
    ret = []
    for n in ["zeke", "josh", "alex", "carlos", "kevin"]:
        if n == name:
            ret.append(n)
    print(ret)
    return ret


@router.get("/match_letter_before")
def get_first_letter(input_letter: str):
    for n in ["zeke", "josh", "alex", "carlos", "kevin",'amanda']:
        if n[0] == input_letter:
            return n


@router.get("/match_letter")
def get_first_letter(input_letter: str):
    ret = []
    for n in ["zeke", "josh", "alex", "carlos", "kevin",'amanda']:
        if n[0] == input_letter:
            ret.append(n)
    return ret


if __name__ == "__main__":
    user_input = str(input())
    foo = get_users_endpoint(user_input)
    print(foo)
