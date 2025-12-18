"""
QUESTION:
Write a recursive function named `sum_divisible_elements` that takes a list of integers and an index as arguments. The function should calculate the sum of all elements in the list that are divisible by 2, greater than 5, and not divisible by 3 or 4. The function should start checking from the given index.
"""

def sum_divisible_elements(lst, index):
    if index >= len(lst):
        return 0

    if lst[index] % 2 == 0 and lst[index] > 5 and lst[index] % 3 != 0 and lst[index] % 4 != 0:
        return lst[index] + sum_divisible_elements(lst, index + 1)
    else:
        return sum_divisible_elements(lst, index + 1)