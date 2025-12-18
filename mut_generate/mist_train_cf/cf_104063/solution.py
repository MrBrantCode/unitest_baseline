"""
QUESTION:
Write a function `min_prime_number` that takes an unordered array of integers as input and returns the minimum prime number in the array. If the array contains duplicate prime numbers, the function should return the smallest prime number. If the array does not contain any prime numbers, the function should return a message indicating that no prime numbers were found. The function should be able to handle arrays with duplicate numbers and non-prime numbers.
"""

import math

def min_prime_number(arr):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    min_prime = float('inf')
    for num in arr:
        if is_prime(num):
            min_prime = min(min_prime, num)

    if min_prime != float('inf'):
        return min_prime
    else:
        return "No prime numbers found in the array."