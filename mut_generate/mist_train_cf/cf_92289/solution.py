"""
QUESTION:
Write a function `is_sum_present` that takes a list of numbers and a target sum as input, and returns `True` if any two numbers from the list sum up to the target sum, and `False` otherwise. The function must run in O(n) time complexity and O(1) space complexity, where n is the length of the list, and must not use any built-in sorting or searching functions.
"""

def is_sum_present(numbers, target_sum):
    num_set = set()
    for num in numbers:
        if target_sum - num in num_set:
            return True
        num_set.add(num)
    return False