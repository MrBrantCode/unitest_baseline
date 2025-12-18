"""
QUESTION:
Create a function called `fibonacci_prime` that calculates the sum of prime numbers within the Fibonacci sequence up to the nth term and returns the sum along with the total count of prime numbers. The function should optimize performance by minimizing repetitive calculations.
"""

def fibonacci_prime(n):
    def fibonacci(n, memo):
        if memo[n] is not None:
            return memo[n]
        if n == 1 or n == 2:
            result = 1
        else:
            result = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        memo[n] = result
        return result

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    sum_primes = 0
    total_primes = 0
    memo = [None] * (n + 1)
    for i in range(1, n+1):
        fib_n = fibonacci(i, memo)
        if is_prime(fib_n):
            sum_primes += fib_n
            total_primes += 1
    return sum_primes, total_primes