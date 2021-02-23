from typing import List, Tuple
from datetime import datetime
from typing import Dict
import math


def read_solar_data(p: str = None) -> List[Tuple[datetime, float]]:
    ret = []
    with open(
        "/Users/zeke/Documents/jbu/cs2233_in_class/data/756874_system_power_20210221.csv",
        "r",
    ) as fp:
        data = fp.readlines()
    for idx, row in enumerate(data):
        if idx == 0:
            continue
        date, power = row.split(",")
        date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S %z")
        ret.append((date, float(power)))
    return ret


def trunc_datetime(dt: datetime):
    return dt.replace(minute=0, second=0, microsecond=0, tzinfo=None)


def hourly_demand_summary(data: List[Tuple[datetime, float]]) -> Dict[datetime, float]:
    """
    This function will return an hourly breakdown of the dataset. This hourly data will include the hour before meaning datetime(2020,2,1,1,0,0) will range from 01:00 - 01:59
    {
        datetime(2020,2,1,0,0): 0.0,
        datetime(2020,2,1,1,0): 0.0,
        ...,
        datetime(2020,2,7,23,0): 0.0,
    }
    """
    ret = {}
    for date, power in data:
        date = trunc_datetime(date)
        if date in ret:
            ret[date] += power
        else:
            ret[date] = power

    return ret


def round_to_30_minutes(dt: datetime):
    if dt.minute >= 30:
        return dt.replace(minute=30)
    return dt.replace(minute=0)


def thirty_minute_demand_summary(
    data: List[Tuple[datetime, float]]
) -> Dict[datetime, float]:
    """
    This function will return an half hour breakdown of the dataset. This  data will include the hour before meaning datetime(2020,2,1,1,0,0) will range from 01:00:00 - 01:29:59 and the second set will range from 01:30:00 - 01:59:59
    {
        datetime(2020,2,1,0,0): 0.0,
        datetime(2020,2,1,0,30): 10.0,
        datetime(2020,2,1,1,0): 20.0,
        datetime(2020,2,1,1,30): 10.0,
        ...,
        datetime(2020,2,7,23,0): 0.0,
    }
    """
    ret = {}
    for date, power in data:
        date = trunc_datetime(date)
        if date in ret:
            ret[date] += power
        else:
            ret[date] = power

    return ret


if __name__ == "__main__":
    from pprint import pprint

    data = read_solar_data()
    print(hourly_demand_summary(data))
