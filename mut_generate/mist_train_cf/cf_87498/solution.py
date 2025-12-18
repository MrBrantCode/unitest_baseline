"""
QUESTION:
Write a function `find_triplet(array, target)` that takes an array of integers and a target integer as input. The function should return the indices of the first occurrence of three consecutive elements in the array that sum up to the target value. If no such triplet exists, return an empty list.
"""

def find_triplet(array, target):
    # Iterate through the array from index 0 to len(array) - 3
    for i in range(len(array) - 2):
        # Check if the sum of current element and next two elements equals the target
        if array[i] + array[i+1] + array[i+2] == target:
            # Return the indices of the triplet
            return [i, i+1, i+2]
    
    # If no triplet is found, return an empty list
    return []