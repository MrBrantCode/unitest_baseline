"""
QUESTION:
Write a recursive function `binary_search_highest_prime(arr, low, high)` that finds the highest prime number in a sorted array `arr` in ascending order. The function should return the highest prime number found, or -1 if no prime numbers are found. The function must utilize a binary search approach and can use a helper function `is_prime(num)` to check if a number is prime. The function should not exceed the given array bounds, where `low` is the starting index and `high` is the ending index.
"""

def binary_search_highest_prime(arr, low, high):
    if high < low:
        return -1
    
    mid = (low + high) // 2
    if is_prime(arr[mid]):
        if mid == high or not is_prime(arr[mid+1]):
            return arr[mid]
        else:
            return binary_search_highest_prime(arr, mid+1, high)
    elif arr[mid] < 2 or not is_prime(arr[mid]):
        return binary_search_highest_prime(arr, low, mid-1)
    else:
        return -1

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True