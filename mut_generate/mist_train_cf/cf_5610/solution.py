"""
QUESTION:
Write a function called `largest_prime` that takes an array of integers as input and returns a tuple containing the largest prime number in the array and its index. If the array is empty or contains only non-prime numbers, the function should return 0 as the largest prime number and -1 as the index. If there are multiple largest prime numbers, the function should return the index of the first occurrence.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def largest_prime(arr):
    max_prime = 0
    max_prime_index = -1

    for i, num in enumerate(arr):
        if is_prime(num):
            if num > max_prime:
                max_prime = num
                max_prime_index = i
    return max_prime, max_prime_index