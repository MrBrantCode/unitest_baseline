"""
QUESTION:
Create a function `copy_array(arr)` that returns a new array consisting of all odd elements from the input array `arr` that are smaller than 5. The function should be implemented recursively and the length of the new array should not exceed 5. If no such elements exist, return an empty array.
"""

def copy_array(arr):
    # Base case: if the input array is empty, return an empty array
    if len(arr) == 0:
        return []
    
    # Base case: if the length of the new array exceeds 5, return an empty array
    if len([x for x in arr if x < 5 and x % 2 != 0]) > 5:
        return []
    
    # Recursive case: check if the first element is smaller than 5 and odd
    if arr[0] < 5 and arr[0] % 2 != 0:
        # Create a new array by concatenating the first element with the result of the recursive call on the rest of the array
        return [arr[0]] + copy_array(arr[1:])
    else:
        # Return the result of the recursive call on the rest of the array
        return copy_array(arr[1:])