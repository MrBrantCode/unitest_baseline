"""
QUESTION:
Implement a function named `sumOfSquares` that takes an array of integers as input and returns the sum of the squares of all the prime numbers in the array. The array may contain negative integers, and the function should ignore any non-prime numbers. The function should also handle edge cases where the array is empty or contains no prime numbers.
"""

def sumOfSquares(arr):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    total = 0
    for num in arr:
        if is_prime(num):
            total += num**2

    return total