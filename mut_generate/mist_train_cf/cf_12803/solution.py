"""
QUESTION:
Write a function named `sum_set_numbers` that takes a set of positive numbers as input. The function should return the sum of all numbers in the set. If the input set is empty, return 0. The function should have a time complexity of O(n), where n is the size of the set.
"""

def sum_set_numbers(my_set):
    total = 0
    if not my_set:
        return 0
    for num in my_set:
        total += num
    return total