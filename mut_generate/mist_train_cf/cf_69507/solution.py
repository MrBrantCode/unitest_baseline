"""
QUESTION:
Create a function `find_min_prime` that takes a list of integers as input and returns the smallest prime number in the list. The function should return `None` if no prime number is found.
"""

def find_min_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    min_prime = None
    for num in numbers:
        if is_prime(num):
            if min_prime is None or num < min_prime:
                min_prime = num

    return min_prime