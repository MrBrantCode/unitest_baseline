"""
QUESTION:
Create a function named `remove_duplicates` that takes an array of integers as input and returns a new array with all duplicate elements removed while preserving the original order of the elements. The input array can contain both positive and negative integers ranging from -10^6 to 10^6, and its length should be less than or equal to 10^6.
"""

def remove_duplicates(data):
    unique_elements = set()
    result = []
    
    for element in data:
        if element not in unique_elements:
            unique_elements.add(element)
            result.append(element)
    
    return result