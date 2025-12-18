"""
QUESTION:
Write a function called `sum_of_divisible_by_three` that calculates the sum of integer values in a given list that are divisible by 3. The list can contain any type of elements, including nested lists. The function should ignore non-integer elements and return the sum as a floating-point number rounded to two decimal places.
"""

def sum_of_divisible_by_three(lst):
    total = 0

    for e in lst:
        if isinstance(e, int) and e % 3 == 0:
            total += e
        elif isinstance(e, list):
            total += sum_of_divisible_by_three(e)

    return round(total, 2)