"""
QUESTION:
Create a function named `fibonacci_series` that takes an integer `n` as input and returns a list of Fibonacci numbers from 0 to `n`. The function should use a purely iterative approach without using recursion or any built-in functions or libraries.
"""

def fibonacci_series(n):
    if n <= 0:
        return []

    series = [0, 1]  

    while len(series) <= n:  
        next_num = series[-1] + series[-2]  
        series.append(next_num)

    return series[:n+1]  