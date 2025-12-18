"""
QUESTION:
Write a function `is_sorted_descending_prime(arr)` that takes an array of integers as input and returns `True` if the array is sorted in descending order with all prime numbers, and `False` otherwise. The function should have a time complexity of O(n) and space complexity of O(1), where n is the length of the array.
"""

def is_sorted_descending_prime(arr):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

    if len(arr) == 0:
        return False
    for i in range(len(arr)-1):
        if arr[i] <= arr[i+1] or not is_prime(arr[i]):
            return False
    return is_prime(arr[-1])