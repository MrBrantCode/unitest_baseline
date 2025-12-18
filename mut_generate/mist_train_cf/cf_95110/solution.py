"""
QUESTION:
Create a function `prime_index_and_value` that takes a list of integers as input and returns a list of elements where the index and the element itself are both prime numbers. The function should handle lists of any length and contain all necessary prime-checking logic.
"""

def prime_index_and_value(arr):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    return [element for index, element in enumerate(arr) if is_prime(index) and is_prime(element)]