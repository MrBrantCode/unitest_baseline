"""
QUESTION:
Write a function `calculate_sum(n)` that takes an integer `n` and returns the sum of all integers from 0 to `n`. Then use this function in a loop to print the numbers from 0 to 4 along with their corresponding sum. However, the function is not being called correctly. Identify and classify the type of error in this code. The function definition is `def calculate_sum(n): return sum(range(n))`.
"""

def calculate_sum(n):
    return sum(range(n + 1))