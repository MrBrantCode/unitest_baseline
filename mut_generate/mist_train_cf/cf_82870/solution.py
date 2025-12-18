"""
QUESTION:
Design a function `fibonacci_prime(n)` that generates the Fibonacci sequence up to the nth term and returns the prime numbers in that sequence. The function should be able to handle error scenarios when the input is not an integer or less than 0, and return an error message in such cases.
"""

def fibonacci_prime(n):
    def fibonacci_sequence(n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        else:
            seq = fibonacci_sequence(n - 1)
            seq.append(seq[-1] + seq[-2])
            return seq

    def is_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        max_divisor = int(num ** 0.5)
        for d in range(3, 1 + max_divisor, 2):
            if num % d == 0:
                return False
        return True

    if not isinstance(n, int) or n < 0:
        return "Error: Input is not a non-negative integer"
    sequence = fibonacci_sequence(n)
    primes = [num for num in sequence if is_prime(num)]
    return primes