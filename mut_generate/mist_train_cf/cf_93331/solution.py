"""
QUESTION:
Write a function `find_common_elements(arr1, arr2)` that takes two arrays of integers as input and returns an array of common elements in ascending order, without duplicates. The function should have a time complexity less than O(n^2), where n is the length of the longer array.
"""

def find_common_elements(arr1, arr2):
    set1 = set(arr1)  # store unique elements from arr1
    set2 = set()  # store common elements
    
    for num in arr2:
        if num in set1:
            set2.add(num)
    
    return sorted(list(set2))