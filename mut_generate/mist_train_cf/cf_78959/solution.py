"""
QUESTION:
Write a function `number_sum(input_dict)` that calculates the sum of all numbers in a nested dictionary and the sum of numbers in nested dictionaries separately. The function should handle dictionaries of arbitrary depth and ignore non-numeric values. It should return the total sum of numbers and the sum of numbers in nested dictionaries.
"""

def entrance(input_dict):
    # Variables to keep track of sum 
    sum_total = 0
    sum_dicts = 0

    # Traversing the dictionary
    for key, value in input_dict.items():
        # If value is number
        if isinstance(value, (int, float)):
            sum_total += value

        # If value is dictionary
        elif isinstance(value, dict):
            # Recursive call
            total, dicts = entrance(value)
            sum_total += total
            sum_dicts += total + dicts

        # If value is not a number or dict
        else:
            # Do nothing
            continue

    # Return sum of numbers and dictionaries individually
    return sum_total, sum_dicts