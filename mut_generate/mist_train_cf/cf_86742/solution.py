"""
QUESTION:
Implement a function named `shift_array` that takes an array as input, removes the first element, and shifts the remaining elements to fill the empty space. The function should not use any built-in array functions, except for accessing and modifying elements, and should not use any additional data structures. The function should have a time complexity of O(n), where n is the size of the array.
"""

def shift_array(arr):
    if len(arr) <= 1:  
        return arr

    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]  

    arr.pop()  

    return arr