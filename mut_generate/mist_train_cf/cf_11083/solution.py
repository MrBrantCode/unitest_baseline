"""
QUESTION:
Write a function `findCommonElements` that takes two arrays `array1` and `array2` as input and returns an array of common elements found in both arrays. The function should have a time complexity of O(n), where n is the size of the larger array, and should not use any additional data structures besides a dictionary and a list. The function should also ensure that no duplicate common elements are included in the output array.
"""

def findCommonElements(array1, array2):
    commonElements = []
    dictionary = {}
    
    for element in array1:
        dictionary[element] = False
    
    for element in array2:
        if element in dictionary and not dictionary[element]:
            dictionary[element] = True
            commonElements.append(element)
    
    return commonElements