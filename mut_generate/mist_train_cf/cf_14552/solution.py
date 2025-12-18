"""
QUESTION:
Write a function `count_occurrences` that takes a float number and a list as input and returns the number of occurrences of the number in the list, excluding any occurrences within sublists. If the input number is not a valid float, return an error message. The function should handle float numbers and ignore non-float numbers in the list.
"""

def count_occurrences(num, lst):
    count = 0
    if not isinstance(num, float):
        return "Error: Number is not a valid float"
    for item in lst:
        if isinstance(item, list):
            continue
        if isinstance(item, float) and item == num:
            count += 1
    return count