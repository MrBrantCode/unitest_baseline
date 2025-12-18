"""
ORIGINAL QUESTION:
Write a function `find_duplicates(arr)` that finds all elements that appear more than once in a given array, returns them in ascending order, and removes any duplicates from the result. Do not use any built-in functions or libraries to solve this problem. Assume the input array has a maximum length of 10^5.
"""

def find_duplicates(arr):
    unique_elements = set()
    duplicates = []
    
    for element in arr:
        if element in unique_elements:
            if element not in duplicates:
                duplicates.append(element)
        else:
            unique_elements.add(element)
    
    duplicates.sort()
    
    return duplicates