"""
QUESTION:
Write a function `sumPositiveIntegers` that accepts an array of integers as input, sums up only the integers greater than 1000, and returns the sum. The function should not include any error handling for non-integer or non-positive inputs. The input array will only contain integers.
"""

def sumPositiveIntegers(numbers):
    sum = 0
    for num in numbers:
        if num > 1000:
            sum += num
    return sum