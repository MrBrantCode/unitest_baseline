"""
QUESTION:
Write a function `sum_within_bounds_average_and_min_val` that determines if the sum of all elements in a list of integers falls within a given range and the average of the list elements is greater than a certain value, and also checks if every element in the list is greater than a specific number. The function should take a list `l` and four parameters: `lower_bound` and `upper_bound` that specify the range for the sum, `min_average` that specifies the minimum average, and `min_val` that specifies the minimum value for each element. The function should return `True` if all conditions are met, and `False` otherwise.
"""

def sum_within_bounds_average_and_min_val(l: list, lower_bound: int, upper_bound: int, min_average: float, min_val: int):
    if not l:
        return False
    total = sum(l)
    if total < lower_bound or total > upper_bound:
        return False
    average = total / len(l)
    if average < min_average:
        return False
    return all(x > min_val for x in l)