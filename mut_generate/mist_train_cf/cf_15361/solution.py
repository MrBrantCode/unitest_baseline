"""
QUESTION:
Create a function called `calculate_sum` that takes a list of integers as input, removes duplicates, and returns the sum of the unique elements if all numbers are positive. If the list is empty, return 0. If the list contains any negative numbers, return -1.
"""

def calculate_sum(input_list):
    unique_list = list(set(input_list))
    if len(unique_list) == 0:
        return 0
    elif any(num < 0 for num in unique_list):
        return -1
    else:
        return sum(unique_list)