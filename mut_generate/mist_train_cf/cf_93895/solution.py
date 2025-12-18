"""
QUESTION:
Design a function named `sum_greater_than_10` that takes an array of numbers as input and returns the sum of all numbers greater than 10 in the array. The function should ignore all numbers less than or equal to 10 and only include numbers greater than 10 in the sum.
"""

def sum_greater_than_10(arr):
    total = 0
    for num in arr:
        if num > 10:
            total += num
    return total