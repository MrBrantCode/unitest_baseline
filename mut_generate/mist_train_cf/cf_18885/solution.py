"""
QUESTION:
Create a function `sum_of_primes` that takes two positive integers `m` and `n` as input, where `m` < `n`, and returns the sum of all prime numbers that can be expressed as the sum of two consecutive Fibonacci numbers in the range from `m` to `n` inclusive. The function should use a helper function `is_prime` to check if a number is prime and another helper function `fibonacci_numbers` to generate Fibonacci numbers within the given range.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci_numbers(m, n):
    fib_numbers = [0, 1]
    while fib_numbers[-1] <= n:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    fib_numbers = fib_numbers[2:]
    return [x for x in fib_numbers if x >= m and x <= n]

def sum_of_primes(m, n):
    fib_numbers = fibonacci_numbers(m, n)
    prime_sums = []
    for i in range(len(fib_numbers) - 1):
        if is_prime(fib_numbers[i] + fib_numbers[i+1]):
            prime_sums.append(fib_numbers[i] + fib_numbers[i+1])
    return sum(prime_sums)