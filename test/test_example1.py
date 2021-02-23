import pytest
from datetime import datetime
from examples.example1 import (
    hourly_demand_summary,
    thirty_minute_demand_summary,
    round_to_30_minutes,
)

default_data = [
    (datetime(2021, 2, 23, 9, 35), 9),
    (datetime(2021, 2, 23, 9, 40), 9),
    (datetime(2021, 2, 23, 10, 5), 10),
]


def test_hourly_demand_function():
    output = hourly_demand_summary(default_data)
    key = datetime(2021, 2, 23, 9, 0)
    assert key in output.keys(), "we should only have hour keys"
    assert output[key] == 18, "we should have 9 w of power"
    assert len(output.keys()) == 2


def test_multiple_hours_works():
    output = hourly_demand_summary(default_data)
    assert len(output.keys()) == 2


@pytest.mark.skip
def test_30_mim_demand():
    data = [
        (datetime(2021, 2, 1, 1, 0), 1),
        (datetime(2021, 2, 1, 2, 0), 4),
        (datetime(2021, 2, 1, 2, 30), 4),
        (datetime(2021, 2, 1, 1, 29), 2),
    ]
    output = thirty_minute_demand_summary(data)

    assert len(output.keys()) == 2
    assert datetime(2021, 2, 1, 1) in output.keys()
    assert datetime(2021, 2, 1, 2) in output.keys()
    assert datetime(2021, 2, 1, 1, 30) in output.keys()
    assert output[datetime(2021, 2, 1, 1, 1)] == 3


def test_round_to_30():
    dt = datetime(2020, 1, 1, 1, 29)
    assert datetime(2020, 1, 1, 1, 0) == round_to_30_minutes(dt)


def test_round_to_30_if_above():
    dt = datetime(2020, 1, 1, 1, 40)
    assert datetime(2020, 1, 1, 1, 30) == round_to_30_minutes(dt)
