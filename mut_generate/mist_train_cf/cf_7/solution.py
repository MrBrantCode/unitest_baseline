"""
QUESTION:
Write a function named `max_prime_difference` that takes an array of integers as input and returns the maximum absolute difference between any two prime numbers in the array. The function should have a time complexity of O(n), where n is the length of the array. It should not use any built-in functions or libraries to check if a number is prime, and it should handle arrays of any length that contain both positive and negative integers. If there are less than two prime numbers in the array, the function should return 0.
"""

def max_prime_difference(arr):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = []
    for num in arr:
        if is_prime(abs(num)):
            primes.append(abs(num))
    if len(primes) < 2:
        return 0
    max_diff = 0
    for i in range(len(primes)-1):
        diff = abs(primes[i] - primes[i+1])
        if diff > max_diff:
            max_diff = diff
    return max_diff