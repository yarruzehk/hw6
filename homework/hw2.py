from typing import Optional, List, Any


def number_length(num: int) -> int:
    """
    Create a function that takes a number and returns its length.
    :param num:
    :return:

    examples:
    number_length(10) -> 2
    number_length(5000) -> 4
    number_length(0) -> 1
    """
    return len(str(num))


def list_of_multiples(num: int, length: Optional[int]) -> List[int]:
    """
    Create a function that takes two numbers as arguments (num, length)
    and returns a list of multiples of num until the list length reaches length.
    :param num:
    :param length:
    :return:

    list_of_multiples(7, 5) -> [7, 14, 21, 28, 35]
    list_of_multiples(12, 10) -> [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
    ist_of_multiples(4, None) -> []
    """

    def foo():
        for i in range(length):
            yield i * num + num

    return list(foo()) if length else []


def normalize(input_str: str) -> str:
    """
    Create a function that takes a string. If the string is all uppercase characters,
     convert it to lowercase and add an exclamation mark at the end.

    :param input_str:
    :return:
    normalize("CAPS LOCK DAY IS OVER") -> "Caps lock day is over!"
    normalize("Today is not caps lock day.") -> "Today is not caps lock day."

    """
    if all(s.isupper() for s in input_str.split()):
        o = []
        for i, s in enumerate(input_str.split()):
            if i == 0:
                o.append(s.title())
                continue
            o.append(s.lower())

        return " ".join(o) + "!"

    return input_str


def cat_dog(num: int) -> str:
    """
    Create a function that takes a number as an argument and returns "Cat", "Dog" or "CatDog".

    If the number is a multiple of 3 the output should be "Cat".
    If the number given is a multiple of 5, the output should be "Dog".
    If the number given is a multiple of both 3 and 5, the output should be "CatDog".
    If the number is not a multiple of either 3 or 5, the number should be output
    on its own as shown in the examples below.
    The output should always be a string even if it is not a multiple of 3 or 5.

    :param num:
    :return:
    cat_dog(4) -> "4"
    cat_dog(3) -> "Cat"
    cat_dog(5) -> "Dog"
    cat_dog(15) -> "CatDog"
    """
    ret = ""
    if num and not num % 3:
        ret += "Cat"
    if num and not num % 5:
        ret += "Dog"
    if not ret:
        ret = str(num)
    return ret
