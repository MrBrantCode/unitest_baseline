"""
QUESTION:
Write a function `prime_difference` that takes a list of integers as input, sorts it in descending order, and returns the difference between the largest and smallest prime numbers. If the list contains no prime numbers, the function should return "No prime numbers found."
"""

def prime_difference(list_of_numbers):
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True

    primes = sorted([num for num in list_of_numbers if is_prime(num)], reverse=True)
    if not primes:
        return "No prime numbers found."
    else:
        return primes[0] - primes[-1]