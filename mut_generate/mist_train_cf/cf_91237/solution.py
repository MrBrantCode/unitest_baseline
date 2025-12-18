"""
QUESTION:
Create a function `delete_element(arr, index)` that takes in an array and an index as input, and returns the modified array after deleting the element at the given index and shifting all the elements after the deleted element to fill the gap. The function should handle invalid index values by returning an error message.
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