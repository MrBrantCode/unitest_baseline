"""
QUESTION:
Write a function `sum_of_multiples_of_three` that calculates the sum of all elements in a given list that are multiples of 3. The list can contain positive and negative integers, and may include duplicates.
"""

def sum_of_multiples_of_three(lst):
    """Calculates the sum of all elements in a given list that are multiples of 3."""
    return sum(num for num in lst if num % 3 == 0)