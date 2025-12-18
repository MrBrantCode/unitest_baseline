"""
QUESTION:
Write a function `sum_of_squares(n)` that takes an integer `n` as input and returns the sum of the squares of all numbers from 1 to `n`. The function should have a time complexity of O(n).
"""

def sum_of_squares(n):
    sum = 0
    for i in range(1, n+1):
        sum += i*i
    
    return sum