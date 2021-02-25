from datetime import datetime
from pprint import pprint

from homework.hw3 import (
    read_solar_data,
    hourly_demand_summary,
    daily_demand_summary,
    weekly_power_summary,
    max_average_power_produced,
    maximum_hourly_data,
)

p = "./data/756874_system_power_20210221.csv"


def test_max_average_power_produced():
    data = read_solar_data(p)
    demand = maximum_hourly_data(data)
    assert demand == datetime(2021, 2, 20, 11, 0)


def test_max_power_produced():
    data = read_solar_data(p)
    demand = max_average_power_produced(data)
    assert type(demand) == tuple
    assert type(demand[0]) == datetime
    assert type(demand[1]) == float


def test_hourly_demand_summary():
    data = read_solar_data(p)
    demand = hourly_demand_summary(data)
    pprint(demand)
    assert type(demand) == dict, "output data type must be dict"
    assert (
        demand[datetime(2021, 2, 19, 12)] == 106537.0
    ), "power produced at 12PM on Feb. 19, 2021"


def test_daily_demand_summary():
    data = list(read_solar_data(p))
    demand = daily_demand_summary(data)
    pprint(demand)
    assert type(demand) == dict, "output data type must be dict"
    assert demand[datetime(2021, 2, 21)] == 72498.0, "power produced on Feb. 6, 2021"


def test_weekly_summary():
    data = list(read_solar_data(p))
    demand = weekly_power_summary(data)
    pprint(demand)
    assert type(demand) == dict, "output data type must be dict"
    assert demand[datetime(2021, 2, 21)] == 2987365.0, "power produced on Feb. 6, 2021"
