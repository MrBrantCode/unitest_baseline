"""
QUESTION:
Write a function called `calculate_sum` that takes in a list of elements as input. The function should calculate and return the sum of all numeric elements in the list, including elements from nested lists, tuples, dictionaries, sets, and strings that can be converted to numbers. The function should handle both positive and negative integers, as well as floating-point numbers, and return the sum as a floating-point number rounded to 2 decimal places. The function should ignore non-numeric elements and None values.
"""

def calculate_sum(lst):
    total = 0.00
    
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
            total += calculate_sum(item)
        elif isinstance(item, dict):
            total += calculate_sum(item.values())
    
    return round(total, 2)