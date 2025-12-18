"""
QUESTION:
Write a function named `find_elements` that takes an array of strings as input and returns a list of unique elements where each element's last character is 's'. The output list should be in ascending order. The function should have a time complexity of O(n), where n is the length of the input array.
"""

def find_elements(arr):
    unique_elements = set()
    
    for element in arr:
        if element[-1] == 's':
            unique_elements.add(element)
    
    return sorted(unique_elements)