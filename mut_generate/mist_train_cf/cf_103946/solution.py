"""
QUESTION:
Create a function named `delete_third_element` that takes an array as input, deletes the element at index 2, and shifts all remaining elements to the left to fill the empty space. Do not use built-in functions or methods for element deletion. Handle edge cases where the input array is empty or has less than 3 elements by returning the original array. Ensure the solution is efficient for large input arrays and follows good programming practices for readability and maintainability.
"""

def delete_third_element(arr):
    if len(arr) < 3:
        return arr
    
    new_arr = [0] * (len(arr) - 1)
    
    for i in range(len(arr)):
        if i < 2:
            new_arr[i] = arr[i]
        elif i > 2:
            new_arr[i-1] = arr[i]
    
    return new_arr