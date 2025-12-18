"""
QUESTION:
Write a function `sum_of_odd_numbers` that takes an array of integers as input and returns the sum of all odd numbers in the array. The array is guaranteed to contain at least one odd number and will have at most 1000 elements.
"""

def sum_of_odd_numbers(arr):
    sum = 0
    for num in arr:
        if num % 2 != 0:  
            sum += num
    return sum