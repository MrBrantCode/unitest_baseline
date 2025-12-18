"""
QUESTION:
Write a function `rotate_array` that takes two parameters: an array and an integer `N`. The function should rotate the array counter-clockwise by `N` steps without using any built-in or third-party library methods for array manipulation. If `N` is greater than the length of the array, it should rotate by `N % len(arr)` steps.
"""

def rotate_array(arr, N):
    N = N % len(arr)  # To handle N greater than size of array
    # Slice the array to 2 parts and swap their position
    rotated_array = arr[N:len(arr)] + arr[0:N]
    return rotated_array