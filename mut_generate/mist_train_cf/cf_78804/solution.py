"""
QUESTION:
Write a function named `next_prime(n)` that returns the next prime number after `n`. The function should optimize computational efficiency. The input `n` is a given integer.
"""

def next_prime(n):
    def is_prime(num):
        if num <= 1:
            return False
        elif num <= 3:
            return True
        elif num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i = i + 6
        return True

    if n < 2:
        return 2
    if n == 2 or n == 3:
        return n + 1
    if n % 2 == 0:
        n += 1
    else:
        n += 2
    while not is_prime(n):
        n += 2
    return n