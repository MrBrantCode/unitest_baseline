"""
QUESTION:
Create a function named `sum_numbers` that takes an array of numbers as an argument. The function should return the sum of all the numbers in the array that are divisible by 3 and have a remainder of 1 when divided by 4.
"""

def sum_numbers(arr):
    total = 0
    for num in arr:
        if num % 3 == 0 and num % 4 == 1:
            total += num
    return total