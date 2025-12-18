"""
QUESTION:
Write a function called `delete_elements` that takes two parameters, an array `arr` and an `element`, and returns a new array with all occurrences of `element` removed from `arr`. The original array should not be modified.
"""

def delete_elements(arr, element):
    # Create a new array to store the filtered elements
    new_arr = []
    
    # Iterate over each element in the input array
    for i in range(len(arr)):
        # If the element is not equal to the specified element, add it to the new array
        if arr[i] != element:
            new_arr.append(arr[i])
    
    return new_arr