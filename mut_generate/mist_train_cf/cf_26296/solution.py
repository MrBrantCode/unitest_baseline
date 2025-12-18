"""
QUESTION:
Create a function `rotateArray(arr, index)` that rotates the given array in a clockwise direction by a specified index. The function should take two parameters: an array `arr` and an integer `index`. The array should be rotated in place and the function should return the rotated array. The rotation index should be considered in a circular manner, meaning if the index exceeds the length of the array, it should wrap around to the start of the array.
"""

def rotateArray(arr, index):
    n = len(arr)
    temp = [arr[(i + index) % n] for i in range(n)]
    arr[:] = temp
    return arr