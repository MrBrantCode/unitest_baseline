"""
QUESTION:
Implement a function named `find_max_element` that finds the maximum element in a given array without using any built-in sorting functions or methods. The function should have a time complexity less than O(n^2). The input array is not empty.
"""

def find_max_element(arr):
    max_element = arr[0] 
    for num in arr: 
        if num > max_element: 
            max_element = num 
    return max_element