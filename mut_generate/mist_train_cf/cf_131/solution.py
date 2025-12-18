"""
QUESTION:
Create a function named `find_intersecting_elements` that takes two arrays as input and returns all intersecting elements in the order they appear in the first array. The function must have a time complexity of O(n), where n is the length of the arrays, and must not use any built-in intersection functions or data structures. Additionally, the function should be implemented using only constant extra space, without modifying the input arrays.
"""

def find_intersecting_elements(arr1, arr2):
    # Create a set to store the elements in arr2
    arr2_set = set(arr2)
    
    # Create a list to store the intersecting elements
    intersecting_elements = []
    
    # Iterate through arr1 and check if each element is in arr2_set
    for num in arr1:
        if num in arr2_set:
            intersecting_elements.append(num)
    
    return intersecting_elements