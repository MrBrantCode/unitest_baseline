"""
QUESTION:
Write a function named `min_max_avg` that takes a list of integers as input and returns a tuple containing the minimum, maximum, and average values in the list. You cannot use built-in functions or methods such as `min()`, `max()`, `sum()`, `len()`, or `sorted()`. The function should achieve this in O(n^2) time complexity and O(1) space complexity without utilizing any additional data structures.
"""

def min_max_avg(lst):
    min_value = lst[0]
    max_value = lst[0]
    sum_value = 0

    for num in lst:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num
        sum_value += num

    average = sum_value / len(lst)

    return (min_value, max_value, average)