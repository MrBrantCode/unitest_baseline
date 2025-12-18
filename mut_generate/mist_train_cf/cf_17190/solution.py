"""
QUESTION:
Create a function `reverse_matching_elements(array1, array2)` that takes two arrays as input and returns a new array containing elements that are present in both `array1` and `array2`. The returned elements should be in the reverse order of their appearance in `array2`, with no duplicates from `array2`. If there are no matching elements, return an empty array.
"""

def reverse_matching_elements(array1, array2):
    reverse_array2 = array2[::-1]  # Reverse the second array
    result = []
    
    for element in reverse_array2:
        if element in array1 and element not in result:
            result.append(element)
            
    return result