"""
QUESTION:
Create a function `check_prime_divisible` that takes a number as input and checks if it is a prime number within the range of 10,000 to 20,000 and is divisible by both 3 and 5.
"""

def check_prime_divisible(number):
    if 10000 <= number <= 20000 and all(number % i != 0 for i in range(2, int(number**0.5)+1)) and number % 3 == 0 and number % 5 == 0:
        return True
    else:
        return False