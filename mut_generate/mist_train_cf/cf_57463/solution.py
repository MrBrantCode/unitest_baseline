"""
QUESTION:
Create a function named `count_prime_digits(n)` that counts the total number of prime digits (2, 3, 5, and 7) in all integers from 1 to n. The function should take an integer n as input and return the total count of prime digits.
"""

def count_prime_digits(n):
    primes = set('2357')
    count = 0
    for i in range(1, n+1):
        str_i = str(i)
        for digit in str_i:
            if digit in primes:
                count += 1
    return count