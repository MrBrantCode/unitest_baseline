"""
QUESTION:
Write a function called `calculate_sum` that takes in a list of elements as input. The function should calculate the sum of all the numbers in the list and its nested elements, handling various types of input elements. The function should not use any built-in sum() function or library functions to calculate the sum, and it should return the sum as a floating-point number, rounded to 2 decimal places. The function should handle the following types of input elements: integers, floating-point numbers, strings that can be converted to numbers, booleans (treated as 0 or 1), lists, tuples, dictionaries (assuming numeric values), and sets, while ignoring non-numeric elements and None values.
"""

def entrance(lst):
    total = 0
    for item in lst:
        if isinstance(item, (int, float)):
            total += item
        elif isinstance(item, str):
            try:
                total += float(item)
            except ValueError:
                pass
        elif isinstance(item, bool):
            total += int(item)
        elif isinstance(item, (list, tuple, set)):
            total += entrance(item)
        elif isinstance(item, dict):
            total += entrance(item.values())
    return round(total, 2)