"""
QUESTION:
Create a function `get_prime_fibonacci(p)` that determines prime numbers within the Fibonacci series up to the `p`-th term. The input `p` should be a positive integer and is constrained to a maximum value of 20. The function should return a list of prime numbers found within the Fibonacci series.
"""

# function to check if number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# function to get prime numbers within a fibonacci series
def get_prime_fibonacci(p):
    fib_series = [0, 1]
    while len(fib_series) < p:
        fib_series.append(fib_series[len(fib_series) - 1] + fib_series[len(fib_series) - 2])
    return [num for num in fib_series if is_prime(num)]