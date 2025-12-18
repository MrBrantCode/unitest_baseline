"""
QUESTION:
Write a function `reorder_array(arr)` that reorders the input array of integers such that all prime numbers appear before all non-prime numbers. The relative order of prime numbers and non-prime numbers should be maintained. The function should have a time complexity of O(n) and should not use any extra space.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def reorder_array(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        if is_prime(arr[left]):
            left += 1
        elif not is_prime(arr[right]):
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr