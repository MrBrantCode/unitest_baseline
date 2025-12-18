"""
QUESTION:
Write a function `reverse_even_odd` that takes a list of integers as input, reverses the order of its elements, and rearranges them such that all even numbers come first, followed by odd numbers. The function should have a time complexity of O(n) and modify the input list in-place without using any additional space.
"""

def reverse_even_odd(arr):
    next_even, next_odd = 0, len(arr) - 1
    while next_even < next_odd:
        if arr[next_even] % 2 == 0:
            next_even += 1
        else:
            arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
            next_odd -= 1
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] % 2 == 0:
            arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr