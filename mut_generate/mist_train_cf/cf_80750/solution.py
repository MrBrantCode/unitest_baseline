"""
QUESTION:
Create a function named `sort_into_subgroups` that takes a list of integers as input and returns a list of subgroups, where the subgroups are defined as follows: the first subgroup contains numbers that are divisible by 2, the second subgroup contains numbers that are divisible by 3, and the third subgroup contains numbers that are not divisible by either 2 or 3.
"""

def sort_into_subgroups(numbers):
    divisible_by_2 = []
    divisible_by_3 = []
    not_divisible = []

    for num in numbers:
        if num % 2 == 0:
            divisible_by_2.append(num)
        elif num % 3 == 0:
            divisible_by_3.append(num)
        else:
            not_divisible.append(num)

    return [divisible_by_2, divisible_by_3, not_divisible]