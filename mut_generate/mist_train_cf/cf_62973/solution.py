"""
QUESTION:
Write a function `get_divisible_by_five` that takes a list of integers as input, uses the `filter` function to find all numbers divisible by 5, and returns them in ascending order. The input list should be created based on user inputs for the list size and the range of integers. The solution must use standard Python libraries only.
"""

def get_divisible_by_five(list_):
    return sorted(filter(lambda x: x % 5 == 0, list_))