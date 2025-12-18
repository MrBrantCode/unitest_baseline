"""
QUESTION:
Create a function `rotate_array(arr, n)` that takes an array `arr` and an integer `n` as input, and returns a new array where the elements of `arr` are rotated `n` places to the right. The function should handle negative integers, where `-n` represents a rotation to the left. The rotation should wrap around, such that after the nth place, the last element of the array becomes the new first element.
"""

def rotate_array(arr, n):
    n = n % len(arr)  # Handle n > len(arr)
    return arr[-n:] + arr[:-n]