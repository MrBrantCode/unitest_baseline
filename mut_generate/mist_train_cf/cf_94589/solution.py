"""
QUESTION:
Create a function `reverse_matching_elements` that takes two arrays `array1` and `array2` as input and returns the elements that are present in both of them, in the reverse order of their first occurrence in `array2`. The function should ignore any duplicate elements in `array2` and return an empty array if there are no matching elements.
"""

def reverse_matching_elements(array1, array2):
    reverse_array2 = array2[::-1]  # Reverse the second array
    result = []
    
    for element in array1:
        if element in reverse_array2 and element not in result:
            result.append(element)
            
    return result