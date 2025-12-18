"""
QUESTION:
Write a function `count_prime_numbers(arr)` that takes an array of integers as input and returns the count of prime numbers in the array. The function should have a time complexity of O(n^2), where n is the length of the array.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_prime_numbers(arr):
    count = 0
    for num in arr:
        if is_prime(num):
            count += 1
    return count