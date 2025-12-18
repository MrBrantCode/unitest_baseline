"""
QUESTION:
Create a function named `fibonacci_series` that calculates the Fibonacci series from 0 to a given number `n` using a purely iterative approach without recursion or built-in functions. The function should return a list of Fibonacci numbers up to the `n`-th index. The input `n` is a non-negative integer.
"""

def fibonacci_series(n):
    if n <= 0:
        return []

    series = [0, 1]  

    while len(series) <= n:  
        next_num = series[-1] + series[-2]  
        series.append(next_num)

    return series[:n+1] 