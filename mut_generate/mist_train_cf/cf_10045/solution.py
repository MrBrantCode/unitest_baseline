"""
QUESTION:
Write a function called `fibonacci(n)` that generates the Fibonacci series up to the nth term and returns the series and the sum of all even numbers in the series. The function should return an empty list if n is less than or equal to 0.
"""

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fibonacci_series = [0, 1]
    even_sum = 0

    for i in range(2, n):
        fibonacci_series.append(fibonacci_series[i-1] + fibonacci_series[i-2])
        if fibonacci_series[i] % 2 == 0:
            even_sum += fibonacci_series[i]

    return fibonacci_series, even_sum