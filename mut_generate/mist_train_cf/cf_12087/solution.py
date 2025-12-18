"""
QUESTION:
Write a function named `find_max_prime` that takes an array of integers as input. The function should return the maximum prime number present in the array. If no prime number is present in the array, return -1.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_max_prime(arr):
    max_prime = -1
    for num in arr:
        if num > max_prime and is_prime(num):
            max_prime = num
    return max_prime if max_prime != -1 else -1