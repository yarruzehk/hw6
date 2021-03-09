import pytest

from quiz.quiz1 import first


@pytest.mark.parametrize(
    "in_a,cmd,o",
    [
        ([], "start", None),
        ([], "end", None),
        (["a", "z"], "eNd", "z"),
        (["a", "z"], "beginning", None),
        (["a", "z", 0], "end", 0),
    ],
)
def test_first(in_a, cmd, o):
    assert first(in_a, cmd) == o
