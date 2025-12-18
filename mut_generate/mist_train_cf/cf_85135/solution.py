"""
QUESTION:
Create a function `get_smallest_prime` that takes a list of 8 integers as input and returns the smallest prime number in the list. If the list contains non-integer values, the function should return an error message. If the list does not contain any prime numbers, the function should return a message indicating this.
"""

def get_smallest_prime(list_of_numbers):
    def check_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    try:
        primes = [num for num in list_of_numbers if check_prime(num)]
        return min(primes) if primes else "No prime numbers found in list"
    except TypeError:
        return "Error: List contains non-integer values"