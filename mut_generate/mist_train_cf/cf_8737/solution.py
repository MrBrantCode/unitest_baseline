"""
QUESTION:
Create a function named `factorial` that calculates the factorial of a given number using recursion. Then, write a dictionary comprehension that creates a new dictionary containing only the key-value pairs from the input dictionary `data` where the key is a prime number. The value in the new dictionary should be the factorial of the corresponding value in `data`.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)