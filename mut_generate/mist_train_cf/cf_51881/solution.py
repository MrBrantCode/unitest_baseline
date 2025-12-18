"""
QUESTION:
Write a function named sum_primes that computes the accumulated total of every prime number that is either 3 or 5 within the numerical range starting from 0 and going up to n, exclusively. The function should have a time complexity better than O(n^2).
"""

def sum_primes(n):
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    total = 0
    for i in range(n):
        if is_prime(i) and (i == 3 or i == 5):
            total += i
    return total