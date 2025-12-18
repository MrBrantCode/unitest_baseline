"""
QUESTION:
Write a function `count_leap_and_prime_leap_years(year)` that calculates the number of leap years and the number of leap years that are also prime numbers from 1900 up to a given year, and returns these two counts. A year is a leap year if it is divisible by 4, but not by 100, unless it is also divisible by 400. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def count_leap_and_prime_leap_years(year):
    leap_years = [y for y in range(1900, year + 1) if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)]
    prime_leap_years = [y for y in leap_years if is_prime(y)]
    return len(leap_years), len(prime_leap_years)