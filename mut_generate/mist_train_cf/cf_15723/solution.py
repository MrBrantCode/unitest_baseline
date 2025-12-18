"""
QUESTION:
Write a function `find_duplicate_indices(arr)` that detects duplicate values in an array and returns their corresponding indices. The function should have a time complexity of O(n), where n is the length of the array, and a space complexity of O(1). The input array contains only integers between 1 and n.
"""

def find_duplicate_indices(arr):
    duplicate_indices = []
    
    # Traverse the array
    for i in range(len(arr)):
        # Get the absolute value of the current element
        index = abs(arr[i])
        
        # Check if the element at index is positive
        # If positive, mark it as visited by making it negative
        # If negative, it means this index has already been visited,
        # so it's a duplicate
        if arr[index - 1] >= 0:
            arr[index - 1] = -arr[index - 1]
        else:
            duplicate_indices.append(index)
    
    return duplicate_indices