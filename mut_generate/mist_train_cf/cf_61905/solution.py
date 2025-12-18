"""
QUESTION:
Create a function named multiply_abs_primes that takes a list of numbers as input and returns the multiplication result of the absolute values of the prime numbers in the list, excluding any number above 100. The result should be rounded down to the nearest integer. If the list contains no prime numbers, the function should return 1.
"""

def is_prime(n):
    if n < 2 or n != int(n):
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def multiply_abs_primes(lst):
    result = 1
    for num in lst:
        abs_num = abs(num)
        if (abs_num <= 100) and is_prime(abs_num):
            result *= abs_num
    return result