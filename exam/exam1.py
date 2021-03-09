from typing import Iterable, List

# BE CAREFUL OF SCOPE WHEN WORKING ON THESE PROBLEMS
list_of_names: List[str] = [
    "alex",
    "amanda",
    "aaron",
    "charlie",
    "vision",
    "wanda",
    "tommy",
    "sophie",
]

# PROBLEM 1 - 10 pts
# Complete the function below to filter the list_of_names defined on line 1.
# This function will filter the list based on the input_str. If the name starts with
# the input string the result will be included return statement of the function.
def filter_list_of_names(input_str: str) -> List[str]:
    ...


# PROBLEM 2 - 5 pts
# Complete a function below.
# Remove the name "vision" from the list on line 1. Return the remaining items of the list
def remove_vision(input_str: str = None) -> List[str]:
    list_of_names.remove("vision")
    return list_of_names


# PROBLEM 3 - 10 pts
# Complete a function below.
# Return the last matching element of list_of_names that ends with the input_str.
# example if the input_str = 'x' the output would be 'alex'
# example if the input_str = 'a' the output would be 'wanda'
def return_last_match(input_str: str) -> str:
    ...


# BONUS PROBLEM - 100% on the exam
# Write a function named "first" that takes an iterable called items and optional key
# word arguments "default" and "condition" If default and condition are not defined, the function will
# return the first item in the list. If default is defined and a empty list is passed into the function,
# the default value will be returned. This function will return type Any or raise a StopIteration exception.
#
# default will have a annotation of Any
# condition will be of type callable
#
# Everything must be correctly defined on function along with passing many different cases. The best attempt
# of the class will also receive and additional 5 pts on the exam.
def default_filter(x):
    return True


def first(items: Iterable, *, default=..., condition: callable = None):
    condition = condition or default_filter
    try:
        return next(i for i in items if condition(i))
    except StopIteration:
        if default == ...:
            raise
        return default


if __name__ == "__main__":
    print(remove_vision())
    print(remove_vision())
