"""
QUESTION:
Remove the element at the specified index from the array and return the updated array.

The function `remove_element(arr, index)` should take an array of integers `arr` and an index position `index` as input, and return the updated array after removing the element at the specified index. If the index is out of bounds (i.e., less than 0 or greater than or equal to the length of the array) or the array is empty, the function should return the original array unchanged.

The array `arr` can have up to 1000 elements, and each element can be any integer between -10^9 and 10^9 inclusive.
"""

def remove_element(arr, index):
    if index < 0 or index >= len(arr) or len(arr) == 0:
        return arr
    
    arr.pop(index)
    return arr