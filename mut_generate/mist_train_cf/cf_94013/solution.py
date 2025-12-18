"""
QUESTION:
Implement a function named `nested_list_sum` that takes a list containing elements of any type, including nested lists, and returns the sum of all integer values within the list as a floating-point number rounded to two decimal places. The function should ignore non-integer elements and handle nested lists recursively.
"""

def nested_list_sum(lst):
    total_sum = 0
    for item in lst:
        if isinstance(item, int):
            total_sum += item
        elif isinstance(item, list):
            total_sum += nested_list_sum(item)
    return round(total_sum, 2)