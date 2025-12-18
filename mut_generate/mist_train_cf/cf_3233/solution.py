"""
QUESTION:
Write a function called `calculate_sum` that takes a list as input and returns the sum of the numbers in the list, including any nested lists. The function should handle both positive and negative integers and floating-point numbers (which should be rounded to the nearest integer before adding to the sum). The function should use recursion and have a time complexity of O(n), where n is the length of the list.
"""

def calculate_sum(lst):
    total_sum = 0

    for item in lst:
        if isinstance(item, list):
            total_sum += calculate_sum(item)
        elif isinstance(item, float):
            total_sum += round(item)
        else:
            total_sum += item

    return total_sum