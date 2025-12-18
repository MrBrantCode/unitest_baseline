"""
QUESTION:
Create a function `fibonacci_with_primality(n)` that generates a Fibonacci sequence up to the nth element, where each number in the sequence is checked for primality before being included. The function should return a list of Fibonacci numbers that are also prime. The input `n` is a non-negative integer representing the number of elements in the sequence.
"""

def fibonacci_with_primality(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
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