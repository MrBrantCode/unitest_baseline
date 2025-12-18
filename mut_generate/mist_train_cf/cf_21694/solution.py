"""
QUESTION:
Create a recursive function called `fibonacci_reverse` that generates the Fibonacci series up to the given number `n` and returns the series in reverse order without using any built-in functions or libraries for generating the Fibonacci series or reversing the series.
"""

def fibonacci_reverse(n):
    if n <= 1:
        return [n]
    else:
        series = fibonacci_reverse(n - 1)
        series.append(series[-1] + series[-2] if len(series) > 1 else 1)
        return series