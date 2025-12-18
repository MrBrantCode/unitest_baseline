"""
QUESTION:
Create a function called `sum_prime_numbers` that takes an array of integers as input and returns the sum of all prime numbers in the array. If the array does not contain any prime numbers, the function should return 0.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_prime_numbers(arr):
    prime_sum = 0
    for num in arr:
        if is_prime(num):
            prime_sum += num
    return prime_sum