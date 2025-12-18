"""
QUESTION:
Write a function `reorder_array` that takes an array of integers as input and reorders the array such that all prime numbers appear before all non-prime numbers, while maintaining the relative order of the prime numbers and the relative order of the non-prime numbers. The function should have a time complexity of O(n) and should not use any extra space.
"""

def reorder_array(arr):
    left = 0
    right = len(arr) - 1

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    while left < right:
        if is_prime(arr[left]):
            left += 1
        elif not is_prime(arr[right]):
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr