"""
QUESTION:
Create a function called `remove_duplicates` that takes an array of integers, floating-point numbers, strings, and nested arrays as input. The function should recursively flatten the nested arrays, remove duplicates, and return a new array of unique values sorted in descending order. The function should have a time complexity of O(n), where n is the length of the input array, and use O(1) additional space.
"""

def remove_duplicates(arr):
    # Flatten the nested arrays
    flattened_arr = []
    for element in arr:
        if isinstance(element, list):
            flattened_arr.extend(remove_duplicates(element))
        else:
            flattened_arr.append(element)
    
    # Use set to remove duplicates
    unique_values = set(flattened_arr)
    
    # Convert set to list and sort in descending order
    sorted_values = sorted(unique_values, reverse=True)
    
    return sorted_values