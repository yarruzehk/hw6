import pytest

from exam.exam1 import (filter_list_of_names, list_of_names, remove_vision,
                        return_last_match)


# 2.5 PTS
def test_vision_is_not_in_list():
    assert "vision" in list_of_names
    assert "vision" not in remove_vision()


# 2.5 PTS
def test_wanda_in_list():
    assert "wanda" in list_of_names
    assert "wanda" in remove_vision()


# 2PTS
@pytest.mark.parametrize(
    "in_str,out",
    [
        ("x", []),
        ("a", ["alex", "amanda", "aaron"]),
        ("aa", ["aaron"]),
        ("wanda", ["wanda"]),
        (
            "",
            [
                "alex",
                "amanda",
                "aaron",
                "charlie",
                "vision",
                "wanda",
                "tommy",
                "sophie",
            ],
        ),
    ],
)
def test_filter_names(in_str, out):
    assert filter_list_of_names(in_str) == out


# 2PTS
@pytest.mark.parametrize(
    "in_str,out",
    [
        ("x", "alex"),
        ("ie", "sophie"),
        ("a", "wanda"),
        ("lie", "charlie"),
        ("q", None),
    ],
)
def test_return_last_match(in_str, out):
    assert return_last_match(in_str) == out
