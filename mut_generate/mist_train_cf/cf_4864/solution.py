"""
QUESTION:
Write a function named `find_largest_prime` that determines the largest prime number in a sorted array of integers. The function should use bitwise operations to perform calculations or comparisons and have a time complexity of O(log n) and a space complexity of O(1).
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