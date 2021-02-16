# The Solar Project - (Because its not warm enough outside to be speaking about solar power)
#  You will submit this project individually but work collaboratively. You will also be graded as a team meaning
#  if 1 member does not submit the code to their repository, and response on blackboard
#  but the other 3 team members do both parts perfectly. The final grade project will be a 75% for everyone.
#
#  Black Board Submission
#    Submit a review of each member of the as part of the blackboard submission.
#    1. I am not expecting much here, just 2 or 3 sentences reviewing each team member.
#    2. What did you enjoy about the project?
#    3. What did you not enjoy?

#  Code Submission:
#    Use the data set for creating  /data/756874_system_power_20210207.csv
#    Required functions in the git repository are below and should be located under /homework/hw3.py
from datetime import datetime
from typing import Dict


def hourly_demand_summary() -> Dict[datetime, float]:
    """
    This function will return an hourly breakdown of the dataset.
    {
        datetime(2020,2,1,0,0): 0.0,
        datetime(2020,2,1,1,0): 0.0,
        ...,
        datetime(2020,2,7,23,0): 0.0,
    }
    """
    ...


def daily_demand_summary() -> Dict[datetime, float]:
    """
    This function will return an daily breakdown of the dataset.
    {
        datetime(2020,2,1): 0.0,
        datetime(2020,2,2): 0.0,
        ...,
        datetime(2020,2,7): 0.0,
    }
    """
    ...


def weekly_power_summary() -> float:
    """
    Summary of total power produced during the week
    """
    ...


def maximum_hourly_data() -> datetime:
    """
    This function will return hour that produced the maximum total power.
    e.g. datetime(2020,2,1,12): 100
         datetime(2020,2,1,13): 200
    :return datetime(2020,2,1,13)

    """
    ...
