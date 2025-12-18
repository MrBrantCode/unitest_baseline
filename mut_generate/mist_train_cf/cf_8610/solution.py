"""
QUESTION:
Create a function named `pack_characters` that takes a string `input_string` of length between 8 and 20 characters. The function should return an array of 8 unique characters from the input string, preserving their original order and sorted in ascending order based on their ASCII values. The function should have a time complexity of O(n), where n is the length of the string.
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