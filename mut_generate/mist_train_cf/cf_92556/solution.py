"""
QUESTION:
Create a function named `remove_duplicates` that takes an array of elements as input. The function should return a sorted array of unique values from the input array in ascending order, using only O(1) additional space and with a time complexity of O(n), where n is the length of the input array. The input array can contain integers, floating-point numbers, and strings.
"""

def remove_duplicates(arr):
    # Sort the input array in ascending order
    arr.sort()
    
    # Initialize two pointers: one for the current element and one for the next unique element
    current = 0
    next_unique = 1
    
    # Iterate through the array
    while next_unique < len(arr):
        # If the current and next unique elements are different, update the current pointer and store the unique element
        if arr[current] != arr[next_unique]:
            current += 1
            arr[current] = arr[next_unique]
        
        # Move the next unique pointer forward
        next_unique += 1
    
    # Return the unique values in the array (excluding the duplicates)
    return arr[:current+1]