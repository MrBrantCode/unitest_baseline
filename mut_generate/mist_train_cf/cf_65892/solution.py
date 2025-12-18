"""
QUESTION:
Write a function `rotate_array` that takes a 2-dimensional array `arr` and an integer `steps` as input. The function should rotate the elements of the 2-dimensional array to the right by the specified number of steps. If the given number of steps is greater than the total number of elements in the array, the rotation should continue from the beginning of the array. The function should return the rotated 2-dimensional array.

The time complexity of the function should be less than O(n^2), where n is the total number of elements in the array.
"""

from collections import deque

def rotate_array(arr, steps):
    rows = len(arr)
    cols = len(arr[0])
    total_elements = rows * cols
    steps = steps % total_elements
    flat_arr = [arr[i//cols][i%cols] for i in range(total_elements)] 
    queue = deque(flat_arr)
    queue.rotate(steps) 
    rotated_arr = [[queue[i*cols + j] for j in range(cols)] for i in range(rows)]
    return rotated_arr