"""
QUESTION:
Write a function `is_sum_present` that takes a list of numbers and a target sum as input and returns `True` if any two numbers in the list sum up to the target sum, and `False` otherwise. The function should have a time complexity of O(n) and a space complexity of O(1), and it cannot use any built-in sorting or searching functions.
"""

def is_sum_present(numbers, target_sum):
    seen = set()
    for num in numbers:
        complement = target_sum - num
        if complement in seen:
            return True
        seen.add(num)
    return False