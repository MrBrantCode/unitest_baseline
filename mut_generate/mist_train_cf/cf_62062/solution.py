"""
QUESTION:
Create a function called `average_in_interval` that takes a list of integers and two integers representing the lower and upper limits of a range as input. The function should calculate the mean value of the integers in the list and return True if the mean is within the specified range (inclusive) and False otherwise.
"""

def average_in_interval(numbers: list, lower_limit: int, upper_limit: int) -> bool:
    """Returns True if the computed arithmetic mean of the elements in the list numbers lies inside the bounds of lower_limit and upper_limit, inclusively.
    """
    mean = sum(numbers) / len(numbers)
    return lower_limit <= mean <= upper_limit