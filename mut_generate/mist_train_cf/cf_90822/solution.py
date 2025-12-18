"""
QUESTION:
Create a function called `factorial` that calculates the factorial of a given number `n` using recursion. The function should have a time complexity of O(n) and a space complexity of O(n).
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)