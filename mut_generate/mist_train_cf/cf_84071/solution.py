"""
QUESTION:
Develop a function `fibonacci_series(n)` to calculate the nth Fibonacci number using recursion with memoization, and another function `fib_closest_avg(n, avg)` to find the Fibonacci number closest to the given average. The program should prompt the user for an integer input 'n' within the range 3-30 (inclusive), and then calculate and print the first 'n' Fibonacci numbers, their sum, average, and the Fibonacci number closest to the average.
"""

def fibonacci_series(n, computed={0:0, 1:1}):
    if n not in computed:
        computed[n] = fibonacci_series(n-1, computed) + fibonacci_series(n-2, computed)
    return computed[n]

def fib_closest_avg(n, avg):
    fib = [fibonacci_series(i) for i in range(n+1)]
    return min(fib, key=lambda x:abs(x-avg))