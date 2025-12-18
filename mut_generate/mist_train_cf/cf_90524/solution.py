"""
QUESTION:
Write a function called `duplicate_characters` that takes a string as input and returns a string where each unique character from the input string is separated by a comma and space. The function must have a time complexity of O(n), where n is the length of the input string.
"""

def duplicate_characters(string):
    seen = set()
    output = []
    
    for char in string:
        if char not in seen:
            output.append(char)
            seen.add(char)
            
    return ', '.join(output)