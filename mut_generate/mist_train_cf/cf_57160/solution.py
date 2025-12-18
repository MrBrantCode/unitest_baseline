"""
QUESTION:
Write a function called ReverseAndCountPrimes that takes an array of integers as input. The function should reverse the array in-place without using any built-in functions or additional data structures, then count the number of prime numbers in the reversed array and return this count. The function should also define a helper function called IsPrime to check if a number is prime.
"""

def ReverseAndCountPrimes(arr):
    def is_prime(n):
        """Check if a number is prime."""
        if n <= 1:
            return False
        if n == 2:
            return True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Reverse the array in-place
    start, end = 0, len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    # Count the number of prime numbers in the reversed array
    prime_count = sum(1 for num in arr if is_prime(num))
    return prime_count