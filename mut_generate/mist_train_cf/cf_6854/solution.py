"""
QUESTION:
Write a recursive function `binary_search_highest_prime(arr, low, high)` that uses binary search to find the highest prime number in a sorted ascending array. The function should return the highest prime number found or -1 if no prime numbers are found. Assume a helper function `is_prime(num)` is available to check if a number is prime. The array indices range from `low` to `high`.
"""

def binary_search_highest_prime(arr, low, high):
    """
    Uses binary search to find the highest prime number in a sorted ascending array.
    
    Args:
        arr (list): A sorted ascending list of integers.
        low (int): The starting index of the array.
        high (int): The ending index of the array.
    
    Returns:
        int: The highest prime number found in the array, or -1 if no prime numbers are found.
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

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