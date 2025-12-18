"""
QUESTION:
Write a function `calculate_required_rate` that takes the number of arithmetic problems Sheila needs to solve and the time in which she needs to solve them as input, and returns her required minimum rate to accomplish the task in problems per minute.

The function should take two parameters: `problems`, the total number of arithmetic problems, and `time_in_minutes`, the time in minutes to solve the problems. The function should return the required rate in problems per minute.
"""

def calculate_required_rate(problems, time_in_minutes):
    """
    Calculate the required minimum rate to accomplish the task in problems per minute.

    Args:
    problems (int): The total number of arithmetic problems.
    time_in_minutes (int): The time in minutes to solve the problems.

    Returns:
    float: The required rate in problems per minute.
    """
    return problems / time_in_minutes