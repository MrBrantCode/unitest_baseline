"""
QUESTION:
Implement a function named `sum_unique_integers` that takes a list of integers as input and returns the sum of all unique integers in the list. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def sum_unique_integers(lst):
    unique_integers = set()
    total_sum = 0

    for num in lst:
        if num not in unique_integers:
            unique_integers.add(num)
            total_sum += num

    return total_sum