"""
QUESTION:
Write a function `is_isomorphic(string1, string2)` that determines if two input strings are isomorphic, where each character in `string1` maps to a unique character in `string2` and vice versa, without using any pre-made functions. The function should return `True` if the strings are isomorphic and `False` otherwise.
"""

def is_isomorphic(string1, string2):
    # Define two empty dictionaries
    dict1 = {}
    dict2 = {}
    
    # If lengths of strings mismatch, they can't be isomorphic
    if len(string1) != len(string2):
        return False

    for i in range(len(string1)):
        # If character is already stored in dictionary
        if string1[i] in dict1:
            # Check that it maps to the same character in string2
            if dict1[string1[i]] != string2[i]:
                return False
        # If character is not stored, add it to dictionary
        else:
            dict1[string1[i]] = string2[i]
            
        # Same process for second string, mapping in other direction
        if string2[i] in dict2:
            if dict2[string2[i]] != string1[i]:
                return False
        else:
            dict2[string2[i]] = string1[i]

    # If we've gone through all characters and found no mismatches, strings are isomorphic
    return True