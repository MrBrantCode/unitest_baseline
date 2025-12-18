"""
QUESTION:
Design a function `findCommonKeys` that takes two arrays of objects as input. Each object has 'name' and 'age' properties. The function should return an array of common names between the two input arrays, but only consider objects with an age of 30 or more and names that do not contain any letters (neither vowels nor consonants). The returned array should be sorted in descending order based on the name property.
"""

def findCommonKeys(arr1, arr2):
    # Filter objects with age 30 or more and exclude objects with name containing vowels and consonants
    modifiedFilteredArr1 = [obj for obj in arr1 if obj['age'] >= 30 and obj['name'].isalpha() == False]
    modifiedFilteredArr2 = [obj for obj in arr2 if obj['age'] >= 30 and obj['name'].isalpha() == False]
    
    # Find common keys between the modified arrays
    commonKeys = [obj['name'] for obj in modifiedFilteredArr1 if obj['name'] in [o['name'] for o in modifiedFilteredArr2]]
    
    # Sort the common keys in descending order based on the name property
    sortedCommonKeys = sorted(commonKeys, reverse=True)
    
    return sortedCommonKeys