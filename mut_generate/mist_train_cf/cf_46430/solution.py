"""
QUESTION:
Create a function named `intersection` that finds the intersection between two sorted arrays without using built-in set or intersection methods. The function should be able to handle duplicate elements by only including each common element once in the result, and should not include any adjacent duplicate elements in the output. The function should take two parameters, `arr1` and `arr2`, which are the two sorted arrays.
"""

def intersection(arr1, arr2):
    i = 0
    j = 0
    intersection = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            # Only add one of each number to the intersection
            if not intersection or arr1[i] != intersection[-1]:
                intersection.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    
    return intersection