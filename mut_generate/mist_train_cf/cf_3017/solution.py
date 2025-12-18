"""
QUESTION:
Create a function `generate_odd_prime_fibonacci(n)` that generates an array of the first `n` odd Fibonacci numbers greater than 1000 and less than 10000, where each number must also be a prime number.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_odd_prime_fibonacci(n):
    fibonacci = [1, 1]  # Starting Fibonacci sequence
    odd_primes = []

    while len(odd_primes) < n:
        next_fib = fibonacci[-1] + fibonacci[-2]  # Calculate next Fibonacci number
        if next_fib > 10000:
            break
        if next_fib > 1000 and next_fib % 2 != 0 and is_prime(next_fib):  # Check if odd and prime
            odd_primes.append(next_fib)
        fibonacci.append(next_fib)

    return odd_primes[:n]  # Return only the first n numbers