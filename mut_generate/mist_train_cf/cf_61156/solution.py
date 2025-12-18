"""
QUESTION:
Write a recursive function called `fibonacci` that calculates the nth number in the Fibonacci series. The function should be used in conjunction with a while loop to display the first five numbers in the series. Note that the solution should not use dynamic programming or matrix exponentiation, but be aware that this may result in a high time complexity and a potential maximum recursion depth error for large inputs.
"""

def fibonacci(n):
    # base case
    if n <= 1:
       return n
    # recursive case
    else:
       return (fibonacci(n-1) + fibonacci(n-2))