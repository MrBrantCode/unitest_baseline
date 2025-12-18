"""
QUESTION:
Create a function named `is_leap_year_and_prime` that takes an integer as input and returns a string. The function should determine whether the input year is a leap year and a prime number, handling negative numbers and non-integer inputs by returning an error message. The function should not use any built-in libraries or functions for prime number checking.
"""

def is_leap_year_and_prime(year):
    # Check for valid input
    if not isinstance(year, int) or year <= 0:
        return "Invalid input: year must be a positive integer"

    # Check if it's a leap year
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        leap_year = True
    else:
        leap_year = False

    # Check if it's a prime number
    if year <= 1:
        prime_number = False
    else:
        prime_number = True
        for i in range(2, int(year ** 0.5) + 1):
            if year % i == 0:
                prime_number = False
                break

    # Return the result
    if leap_year and prime_number:
        return f"{year} is a leap year and a prime number"
    elif leap_year:
        return f"{year} is a leap year, but not a prime number"
    elif prime_number:
        return f"{year} is not a leap year, but a prime number"
    else:
        return f"{year} is neither a leap year nor a prime number"