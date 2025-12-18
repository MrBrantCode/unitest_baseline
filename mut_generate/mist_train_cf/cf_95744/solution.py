"""
QUESTION:
Write a function `largest_prime(array)` to determine the largest prime number in a sorted array of integers. The function should have a time complexity of O(log n) and a space complexity of O(1).
"""

def largest_prime(array):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if is_prime(array[mid]):
            return array[mid]
        elif array[mid] < 2 or not is_prime(array[mid]):
            right = mid - 1
        else:
            left = mid + 1

    return None