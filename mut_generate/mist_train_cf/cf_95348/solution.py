"""
QUESTION:
Write a function `remove_prime_sort(arr)` that takes a list of integers as input, removes any element that is a prime number, and returns the remaining elements in descending order.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_prime_sort(arr):
    result_list = [num for num in arr if not is_prime(num)]
    return sorted(result_list, reverse=True)