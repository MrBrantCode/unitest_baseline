"""
QUESTION:
Create a recursive function `sum_divisible_by_three` that takes a list of integers as input and returns the sum of the elements in the list that are divisible by 3.
"""

def sum_divisible_by_three(lst):
    # Base case: if the list is empty, return 0
    if len(lst) == 0:
        return 0
    # Recursive case: if the first element is divisible by 3, add it to the sum of the remaining elements
    if lst[0] % 3 == 0:
        return lst[0] + sum_divisible_by_three(lst[1:])
    # Recursive case: if the first element is not divisible by 3, skip it and move to the next element
    else:
        return sum_divisible_by_three(lst[1:])