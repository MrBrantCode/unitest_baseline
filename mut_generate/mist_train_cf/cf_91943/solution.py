"""
QUESTION:
Create a function `find_common_elements(arr1, arr2)` that takes in two sorted arrays of integers and returns a new array containing the common elements between the two arrays. The function should handle arrays of any size, have no duplicate elements in the output array, and achieve a time complexity of O(n), where n is the length of the longer array.
"""

def find_common_elements(arr1, arr2):
    common_elements = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            if not common_elements or common_elements[-1] != arr1[i]:
                common_elements.append(arr1[i])
            i += 1
            j += 1
    
    return common_elements