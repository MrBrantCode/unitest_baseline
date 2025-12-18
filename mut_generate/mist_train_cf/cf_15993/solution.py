"""
QUESTION:
Create a function `nested_list_sum` that calculates the sum of all integer values in a given list, including those in nested lists. The function should ignore non-integer elements and return the sum as a floating-point number rounded to two decimal places.
"""

def nested_list_sum(lst):
    total_sum = 0
    for item in lst:
        if isinstance(item, int):
            total_sum += item
        elif isinstance(item, list):
            total_sum += nested_list_sum(item)
    return round(total_sum, 2)