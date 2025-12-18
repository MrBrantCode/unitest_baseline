"""
QUESTION:
Create a function called `pack_characters` that takes a string of length 8 to 20 characters as input and returns an array of length 8 containing unique characters from the string, sorted in ascending order based on their ASCII values, and preserving their original order of appearance. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def pack_characters(input_string):
    packed_array = []
    unique_characters = set()

    for char in input_string:
        if char not in unique_characters:
            unique_characters.add(char)
            packed_array.append(char)
            
            if len(packed_array) == 8:
                packed_array.sort()
                return packed_array
    
    packed_array.sort()
    return packed_array