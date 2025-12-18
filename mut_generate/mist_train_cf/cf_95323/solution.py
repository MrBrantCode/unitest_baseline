"""
QUESTION:
Insert a new element at the beginning of an existing unsorted array without using any built-in array functions or methods. 

The function should take two parameters: an existing array and a new element. The new element should be placed at the beginning of the array and all other elements should be shifted to the right. The function should return the updated array. 

Assume that the existing array can be of any length, including zero.
"""

def entance(arr, element):
    new_arr = [None] * (len(arr) + 1)
    new_arr[0] = element
    for i in range(len(arr)):
        new_arr[i+1] = arr[i]
    return new_arr