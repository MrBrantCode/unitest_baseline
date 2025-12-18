"""
QUESTION:
Write a function called `max_prime_difference` that takes an array of integers as input and returns the maximum difference between any two prime numbers in the array. The function should handle arrays of any length, include both positive and negative integers, and return the maximum difference as an absolute value. The time complexity of the function should be O(n), where n is the length of the array, and it should not use any built-in functions or libraries to check if a number is prime.
"""

def max_prime_difference(arr):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [abs(num) for num in arr if is_prime(abs(num))]
    if len(primes) < 2:
        return 0
    return max(abs(primes[i] - primes[i+1]) for i in range(len(primes)-1))