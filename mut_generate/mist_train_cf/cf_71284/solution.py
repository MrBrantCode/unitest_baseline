"""
QUESTION:
Create a function called `is_isomorphic` that determines if two input strings are isomorphic. The function should take two parameters, `string1` and `string2`, and return a boolean value indicating whether the strings are isomorphic or not. The function must not use any libraries, recursion, or built-in functions. Two strings are isomorphic if the characters in `string1` can be replaced to get `string2`, where each character in `string1` is replaced by the same character in `string2`, and no two characters in `string1` are replaced by the same character in `string2`.
"""

def is_isomorphic(string1, string2):
    # If lengths of the strings are not same, they can't be isomorphic
    if len(string1) != len(string2): 
        return False
        
    mapping = {}
    mapped_values = []
    
    for char1, char2 in zip(string1, string2):
        if char1 not in mapping:
            # If current char in string2 is already a part of an existing mapping
            # The strings cannot be isomorphic
            if char2 in mapped_values:
                return False
            mapping[char1] = char2
            mapped_values.append(char2)
        elif mapping[char1] != char2:
            return False
    return True