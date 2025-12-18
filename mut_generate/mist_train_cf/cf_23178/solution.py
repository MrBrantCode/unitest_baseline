"""
QUESTION:
Implement a function `sumOfSquares` that calculates the sum of the squares of all prime numbers in the given array. Ignore non-prime numbers and handle edge cases where the array is empty or contains no prime numbers. The array may contain negative integers.
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