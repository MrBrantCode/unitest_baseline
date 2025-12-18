"""
QUESTION:
Create a function `duplicate_characters` that takes a string as input and returns a string of duplicate characters in the input string. The input string only contains lowercase alphabets. Do not use built-in functions or data structures like lists, sets, or dictionaries. The function should have linear time complexity and constant space complexity.
"""

def get_index(char):
    return ord(char) - ord('a')

def duplicate_characters(string):
    visited = ["\0"] * 26 
    duplicates = ["\0"] * 26 
    for char in string:
        index = get_index(char) 
        if visited[index] == "\0": 
            visited[index] = char
        elif visited[index] == char and duplicates[index] == "\0":
            duplicates[index] = char
    
    return ''.join([char for char in duplicates if char != '\0'])