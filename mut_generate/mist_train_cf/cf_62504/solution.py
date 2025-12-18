"""
QUESTION:
Create a function "is_prime" that takes an integer "number" as input and returns "True" if the number is prime and "False" otherwise. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should be efficient and not check all possible divisors.

Create another function "next_prime" that takes an integer "number" as input and returns the smallest prime number greater than the given number. The function should utilize the "is_prime" function to find the next prime number.
"""

def is_prime(number):
    if number < 2:
        return False
    root = int(number ** 0.5)
    for i in range(2, root + 1):
        if number % i == 0:
            return False
    return True

def next_prime(number):
    while True:
        number += 1
        if is_prime(number):
            return number