"""
QUESTION:
Create a function named `find_prime_numbers` that takes an array of integers as input and returns a list of all the prime numbers in the array in descending order. The function must have a time complexity of less than O(n^2), where n is the size of the input array, and must utilize a recursive approach for checking prime numbers.
"""

def find_prime_numbers(arr):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    primes = [num for num in arr if is_prime(num)]
    primes.sort(reverse=True)
    return primes