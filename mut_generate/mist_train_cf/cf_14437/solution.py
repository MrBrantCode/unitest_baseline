"""
QUESTION:
Write a function `remove_non_repeating_elements(arr)` that creates a new array containing the elements from the input array `arr` that appear more than once, without modifying the original array.
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