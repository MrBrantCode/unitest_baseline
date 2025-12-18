"""
QUESTION:
Create a function called `remove_duplicates` that takes an array as input and returns a list of unique values in descending order. The input array can contain integers, floating-point numbers, strings, and nested arrays. The function should handle nested arrays by recursively flattening them before removing duplicates. It should also have a time complexity of O(n) and use O(1) additional space.
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