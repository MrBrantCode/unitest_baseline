"""
QUESTION:
Create a function `sum_of_divisible_by_three` that calculates the sum of all integer values in a list (including nested lists) that are divisible by 3. The function should return the sum as a floating-point number rounded to two decimal places. The input list can contain elements of any type, but only integers divisible by 3 should be included in the sum.
"""

def sum_of_divisible_by_three(lst):
    total = 0

    for e in lst:
        if isinstance(e, int) and e % 3 == 0:
            total += e
        elif isinstance(e, list):
            total += sum_of_divisible_by_three(e)

    return round(total, 2)