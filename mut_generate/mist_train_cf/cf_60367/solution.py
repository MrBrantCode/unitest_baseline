"""
QUESTION:
Write a function named `find_unique_elements_count` that takes two arrays of integers as input, `array1` and `array2`, and returns the count of unique elements in both arrays. The function should not use any preexisting library function for handling collections or arrays. The arrays can be of different lengths and are unsorted.
"""

def find_unique_elements_count(array1, array2):
    unique_elements = {}  

    for element in array1:  
        if element not in unique_elements:  
            unique_elements[element] = None  

    for element in array2:  
        if element not in unique_elements:  
            unique_elements[element] = None  

    return len(unique_elements)  