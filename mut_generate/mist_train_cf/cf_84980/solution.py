"""
QUESTION:
Write a function named 'fibonacci' that generates the first 'n' numbers in the Fibonacci sequence. 'n' should be an integer input greater than zero. The function should validate the input to ensure it's a positive integer and return a descriptive error message otherwise. The function should return a list of the first 'n' Fibonacci numbers if 'n' is valid.
"""

def fibonacci(n):
    # Validate if the input is integer namely n and greater than 0
    if not isinstance(n, int) or n <= 0:
        return "Input should be a positive integer"
    
    result = []
    a, b = 0, 1
    for i in range(n):
        result.append(a)
        a, b = b, a+b
    return result