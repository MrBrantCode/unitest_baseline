"""
QUESTION:
Write a function `find_largest_prime(arr)` to determine the largest prime number in a sorted array of integers. The function should have a time complexity of O(log n) and a space complexity of O(1). It should only use bitwise operations to perform any calculations or comparisons.
"""

def find_largest_prime(arr):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) >> 1
        if is_prime(arr[mid]):
            return arr[mid]
        elif arr[mid] > 2:
            right = mid - 1
        else:
            left = mid + 1

    return None