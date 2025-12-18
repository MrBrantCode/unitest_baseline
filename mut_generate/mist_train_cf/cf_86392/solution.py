"""
QUESTION:
Implement a function `find_min_prime(arr)` that takes an unordered array of integers as input and returns the minimum prime number in the array. The array may contain duplicates. The solution should not use any built-in functions or libraries that directly check for primality. If no prime number is found, the function should return the smallest possible prime value that could be in the array.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def find_min_prime(arr):
    min_prime = float('inf')
    for num in arr:
        if num <= min_prime and is_prime(num):
            min_prime = num
    return min_prime if min_prime != float('inf') else 2