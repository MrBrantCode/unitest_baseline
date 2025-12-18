"""
QUESTION:
Write a function named `remove_duplicates` that takes an array of integers as input and returns a new array containing all the unique elements from the input array in their original order. The function should be able to handle arrays of up to 10^6 elements, with integer values ranging from -10^6 to 10^6.
"""

def remove_duplicates(data):
    unique_elements = set()
    result = []
    
    for element in data:
        if element not in unique_elements:
            unique_elements.add(element)
            result.append(element)
    
    return result