"""
QUESTION:
Write a function named `count_odd_numbers` that takes an array of integers as input and returns the count of odd numbers in the array that are greater than 10 and less than 100.
"""

def count_odd_numbers(arr):
    count = 0
    for num in arr:
        if num > 10 and num < 100 and num % 2 != 0:
            count += 1
    return count