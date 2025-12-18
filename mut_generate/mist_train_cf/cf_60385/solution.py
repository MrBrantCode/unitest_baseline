"""
QUESTION:
Write a function `merge_sort_remove_duplicates` that takes a list of lists of integers as input, merges the lists into one, sorts the resulting list in ascending order without using built-in sort functions, removes duplicates, and returns the resulting list. The function should also handle invalid inputs (non-list or non-integer values) and return an error message.
"""

def merge_sort_remove_duplicates(arrays):
    # Check if input is a list
    if not isinstance(arrays, list):
        return "Error: Input should be a list of lists."

    merged = []
    
    for array in arrays:
        # Check if each array is a list 
        if not isinstance(array, list):
            return "Error: Input should be a list of lists."
        
        # Check if each array contains only integers
        for num in array:
            if not isinstance(num, int):
                return "Error: Each array should contain only integers."
        
        merged.extend(array)

    # Sort using Bubble Sort Algorithm
    for i in range(len(merged)):
        for j in range(0, len(merged) - i - 1):
            if merged[j] > merged[j+1] :
                merged[j], merged[j+1] = merged[j+1], merged[j]
            
    # Remove duplicates
    return list(set(merged))