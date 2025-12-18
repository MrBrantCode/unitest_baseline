"""
QUESTION:
Write a function `find_min(arr)` that finds the minimum element in a given array and returns the minimum element along with its indices. If there are multiple minimum elements, the function should return all of their indices. If the array is empty, the function should return `None, []`.
"""

def find_min(arr):
    if len(arr) == 0:
        return None, []

    min_element = arr[0]
    indices = [0]

    for i in range(1, len(arr)):
        if arr[i] < min_element:
            min_element = arr[i]
            indices = [i]
        elif arr[i] == min_element:
            indices.append(i)

    return min_element, indices