"""
QUESTION:
Write a function named `find_primes` that returns a list of all prime numbers between a given range (inclusive), excluding numbers that are divisible by 2, 3, or 5. The function should take two parameters, `start` and `end`, representing the start and end of the range, respectively.
"""

def find_primes(start, end):
    def is_prime(num):
        if num < 2:
            return False
        if num == 2 or num == 3 or num == 5:
            return True
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes