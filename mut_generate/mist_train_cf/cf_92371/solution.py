"""
QUESTION:
Create a function `rearrange_characters` that takes a string as input, rearranges the characters of each word by shifting them one position forward in the alphabet (wrapping around from 'z' to 'a' or 'Z' to 'A'), and returns the rearranged string. The input string will only contain alphabetic characters and spaces, and the function should handle uppercase and lowercase letters properly.
"""

def rearrange_characters(string):
    words = string.split()
    rearranged_words = []
    
    for word in words:
        rearranged_word = ""
        for char in word:
            if char.islower():
                rearranged_word += chr(ord('a') + (ord(char) - ord('a') + 1) % 26)
            else:
                rearranged_word += chr(ord('A') + (ord(char) - ord('A') + 1) % 26)
        rearranged_words.append(rearranged_word)
    
    rearranged_string = " ".join(rearranged_words)
    return rearranged_string