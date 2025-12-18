"""
QUESTION:
Write a function named `count_occurrences` that takes two parameters: a list of integers `lst` and an integer `value`. The function should return the number of occurrences of `value` in `lst` without using any built-in Python functions or libraries.
"""

def count_occurrences(lst, value):
    count = 0
    for num in lst:
        if num == value:
            count += 1
    return count