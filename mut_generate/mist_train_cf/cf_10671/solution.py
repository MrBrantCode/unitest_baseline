"""
QUESTION:
Write a function `find_common_elements(arr1, arr2)` that compares two given arrays `arr1` and `arr2` and returns a list of common elements present in both, while maintaining their relative order. The function should achieve a time complexity of O(n), where n is the length of the longer array, and a space complexity of O(m), where m is the number of common elements between the two arrays.
"""

def find_common_elements(arr1, arr2):
    if len(arr1) < len(arr2):
        smaller_array = arr1
        larger_array = arr2
    else:
        smaller_array = arr2
        larger_array = arr1
    
    common_elements = []
    smaller_set = set(smaller_array)
    
    for element in larger_array:
        if element in smaller_set:
            common_elements.append(element)
    
    return common_elements