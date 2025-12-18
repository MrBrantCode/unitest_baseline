"""
QUESTION:
Write a function `calculateSum` that calculates the sum of the first n natural numbers. The function should take an integer `n` as input and return the sum of all natural numbers from 1 to `n`.
"""

def calculateSum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum