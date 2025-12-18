"""
QUESTION:
Write a function `max_number` that finds the maximum number in a list of integers without using the built-in `max` function. The function should handle edge cases, including an empty list and a list with a single element or duplicate elements with the maximum value.
"""

def max_number(new_list):
    if len(new_list) == 0:   # Edge case: empty list
        return "The list is empty."
    else:
        max_value = new_list[0]  # Take the first element as initial maximum
        for num in new_list[1:]:
            if num > max_value:
                max_value = num
        return max_value