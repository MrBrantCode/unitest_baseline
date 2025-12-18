"""
QUESTION:
Write a function named `sum_to_n` that takes an integer `n` as input and returns the sum of all prime numbers from 1 to `n` (inclusive). The function should return 0 if `n` is less than or equal to 1.
"""

def sum_to_n(n):
    def is_prime(num):
        if num <= 1: 
            return False
        if num <= 3: 
            return True

        if num % 2 == 0 or num % 3 == 0:
            return False

        for i in range(5, int(num**0.5) + 1, 6):
            if num % i == 0 or num % (i + 2) == 0:
                return False

        return True

    sum = 0
    for i in range(1, n + 1):
        if is_prime(i): 
            sum += i
    return sum