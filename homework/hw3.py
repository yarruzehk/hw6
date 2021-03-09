from collections import defaultdict
from datetime import datetime, timedelta
from typing import Dict, Iterable, List, Tuple


def read_solar_data(
    p: str = "../data/756874_system_power_20210207.csv",
) -> Iterable[Tuple[datetime, float]]:
    with open(p, "r") as fp:
        data = fp.readlines()
    for idx, row in enumerate(data):
        if idx == 0:
            continue
        date, power = row.split(",")
        date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S %z")
        yield date, float(power)


def trunc_date_to_hour(dt: datetime, daily=False):
    if daily:
        return dt.replace(hour=0, minute=0, second=0, tzinfo=None)
    return dt.replace(minute=0, second=0, microsecond=0, tzinfo=None)


def move_to_sunday(dt: datetime):
    dt = trunc_date_to_hour(dt, True) - timedelta(days=dt.weekday()) + timedelta(days=6)
    return dt


def hourly_demand_summary(data: List[Tuple[datetime, float]]) -> Dict[datetime, float]:
    ret = defaultdict(lambda: 0)
    for date, power in data:
        ret[trunc_date_to_hour(date)] += power
    return dict(ret)


def daily_demand_summary(data: List[Tuple[datetime, float]]) -> Dict[datetime, float]:
    ret = defaultdict(lambda: 0)
    for date, power in data:
        ret[trunc_date_to_hour(date, True)] += power
    return dict(ret)


def weekly_power_summary(
    data: List[Tuple[datetime, float]]
) -> List[Dict[datetime, float]]:
    ret = defaultdict(lambda: 0)
    for date, power in data:
        ret[move_to_sunday(date)] += power
    return dict(ret)


def maximum_hourly_data(data: List[Tuple[datetime, float]]) -> datetime:
    demand = hourly_demand_summary(data)
    return max(demand, key=demand.get)


def max_average_power_produced(
    data: List[Tuple[datetime, float]]
) -> Tuple[datetime, float]:
    return max(data, key=lambda x: x[1])
