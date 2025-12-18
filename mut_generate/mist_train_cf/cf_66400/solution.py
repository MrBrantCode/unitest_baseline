"""
QUESTION:
Write a function `calculate_stats(input_dict)` that takes a dictionary of unknown length with integer lists as values. The function should return a new dictionary where each key corresponds to a dictionary containing the sum, average, and standard deviation of each list in the input dictionary. 

The function should handle edge cases such as empty dictionaries, keys with empty lists, or keys with single element lists, and should have a time complexity not greater than O(n), where n is the total number of elements in all lists combined. The function should also be capable of handling large integers to avoid overflow.
"""

import math

def calculate_stats(input_dict):
    result = {}

    for key, value_list in input_dict.items():
        if len(value_list) == 0:
            result[key] = {'sum': 0, 'average': 0, 'std_dev': 0}
            continue

        total = sum(value_list)
        average = total / len(value_list)

        variance = sum((xi - average)**2 for xi in value_list)
        variance = variance / len(value_list)

        std_dev = math.sqrt(variance)

        result[key] = {'sum': total, 'average': average, 'std_dev': std_dev}

    return result