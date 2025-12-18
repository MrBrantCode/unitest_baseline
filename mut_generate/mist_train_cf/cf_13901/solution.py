"""
QUESTION:
Write a function named `delete_elements` that takes an array `arr` and an `element` as input, and returns a new array containing all elements from `arr` except for `element`. The function should not modify the original array and should be able to handle duplicate occurrences of the element to be deleted.
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