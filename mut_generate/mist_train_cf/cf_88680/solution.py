"""
QUESTION:
Implement a function named `rotate_array` that performs an in-place rotation on the input array `arr` by `rotation` number of times. The function should modify the original array and handle both clockwise and counterclockwise rotations. The rotation value is a positive integer. The function should have a time complexity of O(n), where n is the length of the array, and a space complexity of O(1).
"""

def rotate_array(arr, rotation):
    length = len(arr)
    effective_rotation = rotation % length

    if effective_rotation == 0:
        return arr

    def reverse_array(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    if effective_rotation > 0:
        reverse_array(0, length - 1)
        reverse_array(0, effective_rotation - 1)
        reverse_array(effective_rotation, length - 1)
    else:
        reverse_array(0, length - 1)
        reverse_array(0, length - effective_rotation - 1)
        reverse_array(length - effective_rotation, length - 1)