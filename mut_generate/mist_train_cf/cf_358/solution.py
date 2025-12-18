"""
QUESTION:
Implement a function `find_min_prime` that takes an unordered array of integers as input, which may contain duplicates, and returns the minimum prime number in the array without using any built-in functions or libraries that directly check for primality. If no prime number is found, return the result accordingly.
"""

def find_min_prime(arr):
    min_prime = float('inf')
    for num in arr:
        if num <= min_prime:
            is_prime = True
            if num < 2:
                is_prime = False
            else:
                for i in range(2, num):
                    if num % i == 0:
                        is_prime = False
                        break
            if is_prime:
                min_prime = num
    return min_prime