import pytest

from util import count_passing_tests


@pytest.fixture()
def example_pass():
    return """
    ============================= test session starts ==============================
    platform darwin -- Python 3.8.7, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
    collected 20 items

    ../../assignments/hw2/zeke/test/test_hw2.py ....................

    ============================== 20 passed in 0.03s ==============================
    """


@pytest.fixture()
def example_fail():
    return """
    ============================= test session starts ==============================
    platform darwin -- Python 3.8.7, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
    collected 20 items

    ../../assignments/hw2/zeke/test/test_hw2.py ....................

    ============================== 20 failed in 0.11s ==============================
    """


def test_get_passes(example_pass):
    assert count_passing_tests(example_pass) == 20


def test_example_fail(example_fail):
    assert count_passing_tests(example_fail) == 0
