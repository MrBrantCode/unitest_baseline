"""
QUESTION:
Write a function to count the number of unique prime numbers below a given number. The function should take an integer as input and return the count of prime numbers less than the input number. A prime number is a natural number that has exactly two distinct natural number divisors: 1 and itself. 0 and 1 are not considered as prime numbers.
"""

def count_primes(n):
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

    count = 0
    for i in range(2, n):
        if is_prime(i):
            count += 1
    return count