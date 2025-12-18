"""
QUESTION:
Write a function named `find_max_difference` that takes an array of positive integers as input and returns the maximum difference between two prime numbers in the array, along with the two prime numbers that yield the maximum difference. The array will always contain at least two prime numbers. Note that 1 is not considered a prime number.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_max_difference(arr):
    primes = [num for num in arr if is_prime(num)]
    max_diff = 0
    prime1 = primes[0]
    prime2 = primes[0]
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            diff = primes[j] - primes[i]
            if diff > max_diff:
                max_diff = diff
                prime1 = primes[i]
                prime2 = primes[j]
    return max_diff, prime1, prime2