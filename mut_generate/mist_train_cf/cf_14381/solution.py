"""
QUESTION:
Create a function named `sum_of_squares` that takes an integer `n` as input. The function should calculate the sum of the squares of numbers from 0 to `n-1`. The function should have a time complexity of O(n) and a space complexity of O(1), meaning it should only use a constant amount of space that does not grow with the size of the input.
"""

def sum_of_squares(n):
    total = 0
    for i in range(n):
        total += i**2
    return total