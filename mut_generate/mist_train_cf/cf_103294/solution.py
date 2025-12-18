"""
QUESTION:
Write a function named `check_prime_in_range` that takes an integer as input and checks if it is a prime number within the range of 1000 to 2000 (inclusive). The function should print whether the number is a prime number and within the specified range, or not.
"""

def check_prime_in_range(number):
    if number >= 1000 and number <= 2000:
        for i in range(2, int(number/2) + 1):
            if (number % i) == 0:
                return f"{number} is not a prime number"
        return f"{number} is a prime number"
    else:
        return f"{number} is not within the range of 1000 to 2000"