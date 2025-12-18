"""
QUESTION:
Write a function named `count_even_greater_than_10` that takes an array of integers as input and returns the number of elements that are both even and greater than 10.
"""

def count_even_greater_than_10(arr):
    count = 0
    for num in arr:
        if num > 10 and num % 2 == 0:
            count += 1
    return count