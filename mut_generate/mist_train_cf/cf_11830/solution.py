"""
QUESTION:
Create a function named `search_element` that takes an array and an element as input, and returns the index of the first occurrence of the element in the array if it exists, otherwise returns -1. The array can contain duplicate elements and is not guaranteed to be sorted. The function should perform the search efficiently, ideally with a time complexity less than O(n) for subsequent searches.
"""

def search_element(array, element):
    frequency = {}
    for i in range(len(array)):
        if array[i] not in frequency:
            frequency[array[i]] = i
    return frequency.get(element, -1)