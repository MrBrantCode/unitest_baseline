"""
QUESTION:
Implement a function named `delete_third_element` that takes an array `arr` as input and deletes the element at index 2. Shift all the remaining elements to the left to fill the empty space. 

The function should handle edge cases where the input array is empty or has less than 3 elements, in which case the resulting array should be the same as the input array. The function should be able to handle large input arrays efficiently with a time complexity of O(n) and a space complexity of O(1).
"""

def delete_third_element(arr):
    if len(arr) < 3:
        return arr
    for i in range(2, len(arr)-1):
        arr[i] = arr[i+1]
    arr.pop()
    return arr