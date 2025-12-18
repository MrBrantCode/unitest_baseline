"""
QUESTION:
Write a function `get_primes_in_fibonacci(n)` that returns a list of prime numbers in the Fibonacci sequence up to the point where the last Fibonacci number has `n` digits. The function should not include non-prime Fibonacci numbers in the output.
"""

import math

def get_primes_in_fibonacci(n):
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False

        sqr = int(math.sqrt(num)) + 1

        for divisor in range(3, sqr, 2):
            if num % divisor == 0:
                return False
        return True

    fib_nums = [0, 1]
    while len(str(fib_nums[-1])) < n:
        fib_num = fib_nums[-1] + fib_nums[-2]
        fib_nums.append(fib_num)
    return [num for num in fib_nums if is_prime(num)]