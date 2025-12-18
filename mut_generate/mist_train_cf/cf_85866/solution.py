"""
QUESTION:
Create a function `accumulate_totals` that takes an integer `n` as input and returns two totals. The function should calculate the accumulated sum of all integer multiples of 3 and 5 within the numerical range from 0 to `n` (inclusive), and then split this sum into two parts: one for the multiples that are prime numbers and one for the multiples that are non-prime numbers.
"""

def accumulate_totals(n):
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2 or num == 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= num:
            if num % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    prime_total = 0
    non_prime_total = 0
    for i in range(n + 1):
        if i % 3 == 0 or i % 5 == 0:
            if is_prime(i):
                prime_total += i
            else:
                non_prime_total += i
    return non_prime_total, prime_total