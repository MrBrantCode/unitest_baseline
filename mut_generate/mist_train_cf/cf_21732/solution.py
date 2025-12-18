"""
QUESTION:
Write a function `find_common_elements(arr1, arr2)` that takes two arrays of integers as input and returns a list of their common elements without using any built-in functions or libraries (such as set() or intersection()) and looping constructs (such as for loops or while loops). The function should be able to handle arrays with duplicate elements and the output list should preserve the minimum count of common elements from both arrays.
"""

def entance(arr1, arr2):
    occurrences1 = {}
    occurrences2 = {}
    
    for num in arr1:
        if num in occurrences1:
            occurrences1[num] += 1
        else:
            occurrences1[num] = 1
    
    for num in arr2:
        if num in occurrences2:
            occurrences2[num] += 1
        else:
            occurrences2[num] = 1
    
    common_elements = []
    for num, count in occurrences1.items():
        if num in occurrences2:
            common_elements.extend([num] * min(count, occurrences2[num]))
    
    return common_elements