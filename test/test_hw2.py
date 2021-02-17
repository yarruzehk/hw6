from homework.hw2 import number_length, list_of_multiples, normalize, cat_dog
import pytest


@pytest.mark.parametrize(
    "in_num,out_num", [(1, 1), (50, 2), (500, 3), (1000, 4), (1_000_000, 7)]
)
def test_number_length(in_num, out_num):
    assert number_length(in_num) == out_num


@pytest.mark.parametrize(
    "num,length,out_num",
    [(1, None, []), (7, 2, [7, 14]), (3, 3, [3, 6, 9]), (8, 1, [8]), (None, None, [])],
)
def test_list_of_multiples(num, length, out_num):
    assert list_of_multiples(num, length) == out_num


@pytest.mark.parametrize(
    "in_str,out_str",
    [
        ("CAPS LOCK DAY IS OVER", "Caps lock day is over!"),
        ("CAPS LOCK DAY IS OVER.", "Caps lock day is over.!"),
        ("Today is not caps lock day.", "Today is not caps lock day."),
        ("TODAY is not caps lock day.", "TODAY is not caps lock day."),
        ("TODAY IS NOT CAPS lock DAY.", "TODAY IS NOT CAPS lock DAY."),
    ],
)
def test_normalize(in_str, out_str):
    assert normalize(in_str) == out_str


@pytest.mark.parametrize(
    "in_num,out_str",
    [(0, "0"), (3, "Cat"), (5, "Dog"), (15, "CatDog"), (4, "4")],
)
def test_cat_dog(in_num, out_str):
    assert cat_dog(in_num) == out_str
