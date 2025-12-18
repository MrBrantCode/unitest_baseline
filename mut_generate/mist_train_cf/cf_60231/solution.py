"""
QUESTION:
Create a function `cumulative_sum(num_list: list)` that calculates the cumulative sum of a given list, correcting common data type-related errors within the list before executing the summation. The function should convert strings to integers or floats if possible, exclude non-numeric strings and non-numeric data types from summation, and handle exceptions using try/except to continue processing the remaining elements of the list when an error is caught.
"""

def cumulative_sum(num_list: list):
    result = 0
    for i in num_list:
        try:
            float_i = float(i)
            result += float_i
        except ValueError:
            continue
        except TypeError:
            continue
    return result