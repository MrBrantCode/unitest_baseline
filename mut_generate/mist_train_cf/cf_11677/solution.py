"""
QUESTION:
Implement a function `find_max(lst)` to find the maximum number in a list of integers without using any built-in functions or methods. The list may contain negative numbers and the function should handle this case correctly.
"""

def find_max(lst):
    max_value = float('-inf')  # start with a very small value as the maximum

    for num in lst:
        if num > max_value:
            max_value = num

    return max_value