"""
QUESTION:
Implement a function `get_sum` that takes an array of integers and a function `is_prime_func` as input and returns the sum of all prime numbers in the array. The `is_prime_func` function checks if a number is prime. Ensure the `get_sum` function has a time complexity of O(n) and a space complexity of O(1).
"""

def get_sum(arr, is_prime_func):
    total = 0
    for num in arr:
        if is_prime_func(num):
            total += num
    return total