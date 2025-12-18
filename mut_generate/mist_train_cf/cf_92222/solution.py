"""
QUESTION:
Write a function `largest_prime_number(array)` that takes an unordered array of integers as input and returns the largest prime number in the array. If no prime numbers are found in the array, the function should return None.
"""

def largest_prime_number(array):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    largest_prime = None
    for num in array:
        if is_prime(num):
            if largest_prime is None or num > largest_prime:
                largest_prime = num
    return largest_prime