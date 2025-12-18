"""
QUESTION:
Write a function called `reverse_fibonacci` that takes a prime number `n` as input and returns the Fibonacci series in reverse order along with the sum of the series. The function should validate that the input `n` is a prime number. If the input is not a prime number or is negative/zero, the function should return an error message.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def reverse_fibonacci(n):
    if n <= 0 or not is_prime(n):
        return "Error: Input is not a prime number or is negative/zero."
    
    def fibonacci(n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        else:
            series = fibonacci(n - 1)
            series.append(series[-1] + series[-2])
            return series

    fib_series = fibonacci(n)
    fib_series.reverse()
    sum_fib = sum(fib_series)
    
    return fib_series, sum_fib