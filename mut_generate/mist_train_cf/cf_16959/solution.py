"""
QUESTION:
Create a function `is_leap_year_and_prime(year)` that takes an integer `year` as input and returns two boolean values. The function should check whether the given year is a leap year and a prime number without using any built-in libraries or functions for prime number checking. A leap year is defined as a year that is divisible by 4, but not by 100, unless it is also divisible by 400. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def is_leap_year_and_prime(year):
    # Leap year checking
    is_leap = False
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            is_leap = True
    
    # Prime number checking
    is_prime = True
    if year <= 1:
        is_prime = False
    else:
        for i in range(2, int(year**0.5) + 1):
            if year % i == 0:
                is_prime = False
                break

    return is_leap, is_prime