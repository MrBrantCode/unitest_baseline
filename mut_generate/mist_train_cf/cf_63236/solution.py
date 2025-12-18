"""
QUESTION:
Write a function `primes_in_fibonacci(n)` that takes an integer `n` and returns a list of prime numbers that are part of the Fibonacci sequence up to `n`. The function should be efficient and handle inputs where `n` is a positive integer.
"""

def primes_in_fibonacci(n):
    def is_prime(num):
        if num <= 1:
            return False
        elif num == 2:
            return True
        elif num % 2 == 0:
            return False
        else:
            i = 3
            while i * i <= num:
                if num % i == 0:
                    return False
                i += 2
            return True

    fib_seq = [0, 1]
    while fib_seq[-1] + fib_seq[-2] <= n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return [num for num in fib_seq if is_prime(num)]