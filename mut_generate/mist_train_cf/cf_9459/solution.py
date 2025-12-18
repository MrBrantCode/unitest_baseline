"""
QUESTION:
Create a function `findElements` that takes two parameters: an array and a key. Return an object containing the key-value pair where the key is the given object key and the value is the count of the key in the array, but only if the key exists in the array and the array is not empty. The function should remove duplicate values from the array before processing. If the array is empty or the key is not found, return an empty object.
"""

def findElements(array, key):
    if len(array) == 0:
        return {}
    
    unique_array = list(set(array))
    
    if key not in unique_array:
        return {}
    
    return {element: array.count(element) for element in unique_array if element == key}