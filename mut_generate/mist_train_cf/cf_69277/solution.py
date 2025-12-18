"""
QUESTION:
Write a function `prime_fibonacci_indexes(n)` that takes an integer `n` as input and returns a list of tuples, where each tuple contains the index position and the prime number from the first `n` numbers of the Fibonacci sequence. Implement this function without using any in-built or third-party libraries to identify prime numbers or generate Fibonacci sequences.
"""

def prime_fibonacci_indexes(n):
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False

        i = 3
        while i * i <= num:
            if num % i == 0:
                return False
            i += 2

        return True

    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return [(i, fib_sequence[i]) for i in range(n) if is_prime(fib_sequence[i])]