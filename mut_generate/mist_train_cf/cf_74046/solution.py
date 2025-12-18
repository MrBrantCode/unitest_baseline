"""
QUESTION:
Implement a function `within_boundary_sum(numbers: list, lower_limit: int, upper_limit: int)` that takes a list of integers and two integer limits as input. The function should return `True` if the cumulative sum of integers at even indices in the list falls within the range defined by `lower_limit` and `upper_limit` (inclusive), and `False` otherwise. The list must not be empty and must contain an even number of elements.
"""

def within_boundary_sum(numbers: list, lower_limit: int, upper_limit: int) -> bool:
    if len(numbers) % 2 != 0 or len(numbers) == 0:
        return False
    total_sum = 0
    for i in range(0, len(numbers), 2):
        total_sum += numbers[i]
    return lower_limit <= total_sum <= upper_limit