"""
QUESTION:
Write a function `filter_primes` that takes an array of integers as input and returns a new array containing only the prime numbers greater than 2 from the original array. The function should have a time complexity of O(n) and a space complexity of O(n), without using any built-in functions or libraries that directly check for prime numbers.
"""

def filter_primes(arr):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    result = [num for num in arr if is_prime(num) and num > 2]
    return result