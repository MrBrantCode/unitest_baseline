"""
QUESTION:
Create a function `is_leap_year_and_prime(year)` that checks if a given integer `year` is both a leap year and a prime number without using any built-in libraries or functions for prime number checking. The function should return a tuple of two boolean values indicating whether `year` is a leap year and a prime number respectively.
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