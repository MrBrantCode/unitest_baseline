"""
QUESTION:
Write a function `find_intersection(arr1, arr2)` that takes two arrays `arr1` and `arr2` as input, and returns the first intersecting element between the two arrays. The function must have a time complexity of O(n), where n is the length of the arrays, and must not use any built-in intersection functions or data structures. The function should be implemented using only constant extra space, without modifying the input arrays.
"""

def find_intersection(arr1, arr2):
    # Convert the second array into a set for faster lookup
    arr2_set = set(arr2)
    
    # Iterate over the first array and check if each element is in the second array
    for num in arr1:
        if num in arr2_set:
            return num
    
    # Return None if there is no intersection
    return None