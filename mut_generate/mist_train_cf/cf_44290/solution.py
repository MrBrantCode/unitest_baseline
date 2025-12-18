"""
QUESTION:
Write a function called `redistribute_arr` that takes an array of integers as input and returns the array with all prime numbers positioned to the left and non-prime numbers aligned to the right. The function should not sort the prime or non-prime numbers, but simply group them together.
"""

def redistribute_arr(arr):
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    prime = [num for num in arr if is_prime(num)]
    non_prime = [num for num in arr if not is_prime(num)]
    return prime + non_prime