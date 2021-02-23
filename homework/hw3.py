def read_solar_data(p: str) -> List[Tuple[datetime, float]]:
    """
    This function will return data from the csv file. Follow the specific format
    """
    ...

def hourly_demand_summary(data: List[Tuple[datetime,float]]) -> Dict[datetime, float]:
    """
    This function will return an hourly breakdown of the dataset. This hourly data will include the hour before meaning datetime(2020,2,1,1,0,0) will range from 01:00 - 01:59
    {
        datetime(2020,2,1,0,0): 0.0,
        datetime(2020,2,1,1,0): 0.0,
        ...,
        datetime(2020,2,7,23,0): 0.0,
    }
    """
    ...


def daily_demand_summary(data: List[Tuple[datetime, float]]) -> Dict[datetime, float]:
    """
    This function will return an daily breakdown of the dataset. This daily data will include infromation from 00:00:00 - 23:59:59 each day.
    {
        datetime(2020,2,1): 0.0,
        datetime(2020,2,2): 0.0,
        ...,
        datetime(2020,2,7): 0.0,
    }
    """
    ...


def weekly_power_summary(data: List[Tuple[datetime, float]]) -> List[Tuple[datetime,float]]:
    """
    Summary of total power produced during the week. A week will be defined as Sunday 00:00 to Saturday 23:59:59. Be careful on how you determine Saturday and Sunday.
    """
    ...


def maximum_hourly_data(data: List[Tuple[datetime,float]]) -> datetime:
    """
    This function will return hour that produced the maximum total power.
    e.g. datetime(2020,2,1,12): 100
         datetime(2020,2,1,13): 200
    :return datetime(2020,2,1,13)

    """
    ...
    
def max_average_power_produced(data: List[Tuple[datetime,float]]) -> Tuple[datetime, float]:
  """
  Return the max real power from the dataset provided. Also provide the datetime which produced the maximum power. This result should look like datetime(2021,2,1,12,5), 500
  """
  ...