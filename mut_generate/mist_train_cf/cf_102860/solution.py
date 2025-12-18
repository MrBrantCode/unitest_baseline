"""
QUESTION:
Write a function `delete_element` that takes an array `arr` and an index `index` as input. The function should delete the element at the given index from the array and shift all the elements after the deleted element to fill the gap. If the given index is out of range (less than 0 or greater than or equal to the length of the array), the function should return an error message. The function should modify the original array and return the modified array.
"""

def delete_element(arr, index):
    if index < 0 or index >= len(arr):
        return "Invalid index"
    
    # Shift all the elements after the deleted element to fill the gap
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i+1]
    
    # Delete the last element
    arr.pop()
    
    return arr