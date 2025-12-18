"""
QUESTION:
Write a function named `replace_vowels` that takes two parameters: a string and a single character. The function should return the input string with all vowels replaced by the given character. The vowels to be replaced are 'a', 'e', 'i', 'o', 'u' (both lowercase and uppercase). The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

def replace_vowels(string, character):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    replaced_string = ""
    
    for char in string:
        if char in vowels:
            replaced_string += character
        else:
            replaced_string += char
            
    return replaced_string