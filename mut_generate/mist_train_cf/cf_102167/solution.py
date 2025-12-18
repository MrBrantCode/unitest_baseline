"""
QUESTION:
Write a function `count_integers` that takes a list of integers, an integer `value`, and an integer `divisor` as input, and returns the count of integers in the list that are greater than `value` and divisible by `divisor`.
"""

def count_integers(lst, value, divisor):
    count = 0
    for num in lst:
        if num > value and num % divisor == 0:
            count += 1
    return count