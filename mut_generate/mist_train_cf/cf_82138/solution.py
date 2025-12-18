"""
QUESTION:
Write a function `calc_sum(n)` that takes an integer `n` (less than or equal to 1000) and returns two values: the sum of all prime numbers less than `n`, and the sum of the numbers that are both prime and Fibonacci numbers less than `n`.
"""

def calc_sum(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def fibonacci(max_num):
        fib_sequence = [0, 1]
        while fib_sequence[-1] < max_num:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[:-1]

    prime_numbers = [i for i in range(1, n) if is_prime(i)]
    prime_sum = sum(prime_numbers)
    fib_numbers = fibonacci(n)
    fib_prime_numbers = [i for i in prime_numbers if i in fib_numbers]
    fib_prime_sum = sum(fib_prime_numbers)
    return prime_sum, fib_prime_sum