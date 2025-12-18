"""
QUESTION:
Write a function `compare_arrays(arr1, arr2)` that compares two unsorted arrays of integers and returns the number of mismatches along with the indices at which the mismatches occur in both arrays. The arrays can contain duplicate values.
"""

def compare_arrays(arr1, arr2):
    mismatches = 0
    mismatch_indices_arr1 = []
    mismatch_indices_arr2 = []
    
    set1 = set(arr1)
    set2 = set(arr2)
    common_elements = set1.intersection(set2)
    
    for element in common_elements:
        indices_arr1 = [i for i, x in enumerate(arr1) if x == element]
        indices_arr2 = [i for i, x in enumerate(arr2) if x == element]
        
        for index1 in indices_arr1:
            for index2 in indices_arr2:
                if index1 != index2:
                    mismatches += 1
                    mismatch_indices_arr1.append(index1)
                    mismatch_indices_arr2.append(index2)
    
    return mismatches, mismatch_indices_arr1, mismatch_indices_arr2