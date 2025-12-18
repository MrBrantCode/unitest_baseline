"""
QUESTION:
Create a function called `remove_non_repeating_elements` that takes an array as input and returns a new array containing the elements that appear more than once in the input array, without modifying the original array. The function should be able to handle arrays of integers.
"""

def remove_non_repeating_elements(arr):
    # Create a dictionary to count the occurrences of each element
    element_count = {}
    for num in arr:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1
    
    # Create a new array with the non-repeating elements
    new_arr = [num for num in arr if element_count[num] > 1]
    
    return new_arr