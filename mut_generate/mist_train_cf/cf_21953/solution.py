"""
QUESTION:
Write a function `find_second_highest` that takes a list of integers as input and returns the second highest value in the list. If there is no second highest value (i.e., the list has less than two unique elements), the function should return -1.
"""

def find_second_highest(lst):
    # Remove duplicates and sort the list in descending order
    unique_values = sorted(set(lst), reverse=True)

    if len(unique_values) < 2:
        # Return -1 if there is no second highest value
        return -1
    else:
        # Return the second highest value
        return unique_values[1]