"""
QUESTION:
Write a function `find_seventh_prime` that takes an array of integers as input and returns the 7th prime number in the array. The function should ignore non-prime numbers and only consider prime numbers when finding the 7th prime number. If there are less than 7 prime numbers in the array, the function should return -1.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_seventh_prime(arr):
    prime_count = 0
    for num in arr:
        if is_prime(num):
            prime_count += 1
            if prime_count == 7:
                return num
    return -1