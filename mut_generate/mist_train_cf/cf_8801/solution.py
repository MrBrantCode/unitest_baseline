"""
QUESTION:
Write a function named `sumOfSquares` that takes an array of integers as input, calculates the sum of the squares of all prime numbers in the array, and returns the result. Ignore non-prime numbers in the array and handle edge cases where the array is empty or contains no prime numbers. If the array is empty or contains no prime numbers, return 0.
"""

def sumOfSquares(arr):
    def isPrime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    if not arr:
        return 0
    
    primes = [num for num in arr if isPrime(num)]
    
    return sum(prime**2 for prime in primes)