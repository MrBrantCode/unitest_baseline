"""
QUESTION:
Write a function `insert_element` that inserts a new element at the beginning of an existing unsorted array without using any built-in array functions or methods. The function should take two parameters: the existing array `arr` and the new element `element`. The function should return a new array with the inserted element at the beginning, and the original array should remain unchanged.
"""

def insert_element(arr, element):
    new_arr = [None] * (len(arr) + 1)
    new_arr[0] = element
    for i in range(len(arr)):
        new_arr[i+1] = arr[i]
    return new_arr