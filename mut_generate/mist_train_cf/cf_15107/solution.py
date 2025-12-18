"""
QUESTION:
Write a function `is_prime(number)` that checks whether a given number is prime or not. The function should return "Prime" if the number is prime and "Not Prime" if the number is not prime. The function should consider that a prime number is a natural number greater than 1 with no positive divisors other than 1 and itself. The function should work for all natural numbers.
"""

def is_prime(number):
    if number <= 1:
        return "Not Prime"
    for i in range(2, int(number/2)+1):
        if number % i == 0:
            return "Not Prime"
    return "Prime"