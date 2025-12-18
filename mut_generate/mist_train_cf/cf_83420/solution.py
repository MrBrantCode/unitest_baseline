"""
QUESTION:
Write a function called `factorial` that calculates the factorial of a given number and then use it to create a new list that includes the factorial of all elements present in the input list. The function should be able to handle a list of non-negative integers.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)