"""
QUESTION:
Write a function named `find_diff_sum` that takes a list of integers as input. The function should calculate and return the sum of absolute differences between each number in the list and the maximum value if the absolute value of the minimum number in the list is greater than 10, otherwise return the sum of absolute differences between each number in the list and the minimum value. The list will have at least one element.
"""

def find_diff_sum(numbers):
    min_val = min(numbers)
    max_val = max(numbers)

    if abs(min_val) > 10:
        return sum(abs(num - max_val) for num in numbers)
    else:
        return sum(abs(num - min_val) for num in numbers)