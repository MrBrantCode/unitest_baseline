"""
QUESTION:
Create a function `sum_even_numbers(arr)` that takes an array of integers as input and returns the sum of all even numbers in the array. The function should iterate through the array, check each number for evenness, and add it to the total sum if it is even.
"""

def sum_even_numbers(arr):
    sum = 0
    for num in arr:
        if num % 2 == 0:
            sum += num
    return sum