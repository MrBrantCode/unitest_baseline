"""
QUESTION:
Write a recursive function `fibonacci_series` that generates the Fibonacci series up to the nearest number that does not exceed a given input value `val`. The function should take two optional parameters `a` and `b` with default values of 0 and 1 respectively, representing the first two numbers in the Fibonacci series.
"""

def fibonacci_series(val, a = 0, b = 1):
    # Base case: if the next term in the fibonacci series is more than the value
    if a > val:
        return
    else:
        # Print the next term
        print(a)

        # Recursive call to calculate the next term in the fibonacci series
        fibonacci_series(val, b, a+b)