"""
QUESTION:
Implement a function `print_prime_numbers(arr)` that takes an array of integers as input and prints all prime numbers present in the array in ascending order. The function should run in O(n) time complexity and use only constant extra space. The function should also be able to handle large numbers efficiently (up to 10^9), but does not need to handle negative numbers or floating-point numbers.
"""

import math

def print_prime_numbers(arr):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    prime_numbers = [num for num in arr if is_prime(num)]
    prime_numbers.sort()
    for num in prime_numbers:
        print(num)