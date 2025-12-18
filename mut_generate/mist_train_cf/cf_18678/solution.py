"""
QUESTION:
Write a function named `remove_duplicates` to delete all duplicate elements from a given array in-place using a while loop, without utilizing any built-in functions or methods that directly solve the problem, and achieve a time complexity of O(n), where n is the length of the array. The order of the elements in the resulting array does not matter.
"""

def remove_duplicates(arr):
    # Create a set to store the unique elements
    unique_elements = set()
    
    # Create an index variable to keep track of the current position
    index = 0
    
    # Loop through the array
    while index < len(arr):
        # Check if the current element is already in the set
        if arr[index] in unique_elements:
            # If it is, remove it from the array
            arr.pop(index)
        else:
            # If it's not, add it to the set and move on to the next element
            unique_elements.add(arr[index])
            index += 1
    return arr