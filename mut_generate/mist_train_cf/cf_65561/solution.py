"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given non-negative integer `n`. The function should use recursion and return the correct result. What is the big-O time complexity of this function? Assume that the input size is `n`.
"""

def factorial(n):
    if n == 0: 
        return 1
    else: 
        return n*factorial(n-1)