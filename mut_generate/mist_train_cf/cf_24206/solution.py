"""
QUESTION:
Write a function `count_even_numbers` that takes an array of integers as input and returns the count of even numbers in the array using a for loop and an if statement.
"""

def count_even_numbers(arr):
    count = 0
    for num in arr:
        if num % 2 == 0:
            count += 1
    return count