"""
QUESTION:
Write a recursive function named `calculate_fibonacci` that calculates the nth Fibonacci number. The function should take an integer `n` as input and return the corresponding Fibonacci number. The function should use recursion as its primary operation and accurately maintain the Fibonacci calculation.
"""

def calculate_fibonacci(n): 
    if n <= 1:
        return n
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)