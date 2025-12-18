"""
QUESTION:
Write a Python function named `calculate_factorials` that takes a list of integers as input and returns the factorial of the last element in the list. The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
"""

def calculate_factorials(lst):
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
                
    return factorial(lst[-1])