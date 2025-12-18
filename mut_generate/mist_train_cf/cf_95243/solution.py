"""
QUESTION:
Write a function named calculateSum that takes a list of numbers as input, calculates the sum of the numbers without using any built-in sum functions or operators, and returns the result. The function should use a single loop, have a time complexity of O(n), and not use any extra space.
"""

def calculateSum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total