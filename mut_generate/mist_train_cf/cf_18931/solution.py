"""
QUESTION:
Create a function named `reverse_days_of_week` that takes an array of the seven days of the week as input. The function should return the input array sorted in reverse alphabetical order.
"""

def reverse_days_of_week(days):
    return sorted(days, reverse=True)