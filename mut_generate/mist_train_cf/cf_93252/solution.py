"""
QUESTION:
Write a function named `fibonacci_primes` that generates the first `n` prime numbers in the Fibonacci sequence. The function should return a list of prime Fibonacci numbers. The input `n` is the number of prime Fibonacci numbers to generate, and it is a positive integer. The function should not take any other inputs. The output should be a list of integers.
"""

def fibonacci_primes(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        if is_prime(b):
            sequence.append(b)
        a, b = b, a + b
    return sequence