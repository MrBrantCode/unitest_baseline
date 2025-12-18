"""
QUESTION:
Create a function named `fibonacci_series` that takes two parameters: `m` and `n`, where `m` is the starting number of the Fibonacci series and `n` is the number of terms in the series. The function should return two values: the Fibonacci series starting from `m` and containing `n` terms, and the sum of the series. The function should only accept positive integers for `m` and `n` where `m >= 0` and `n >= 2`. If the inputs do not meet these conditions, the function should raise an exception.
"""

def fibonacci_series(m, n):
    if not isinstance(m, int) or not isinstance(n, int) or m < 0 or n < 2:
        raise Exception("m and n must be positive integers and m >= 0 and n >= 2.")
    
    series = [m]
    a, b = m, m
    for _ in range(n-1):
        a, b = b, a + b
        series.append(b)
    
    return series, sum(series)