"""
QUESTION:
Implement a function `shift_array(arr)` that removes the first element from the array and shifts all the remaining elements one position to the left to fill the empty space. The function should not use any built-in array functions (except `len` and indexing) or additional data structures, and it should have a time complexity of O(n), where n is the size of the array. If the array has one or zero elements, the function should return an empty array.
"""

def shift_array(arr):
    if len(arr) <= 1:  
        return []

    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]  

    arr.pop()  

    return arr