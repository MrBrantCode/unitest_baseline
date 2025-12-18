"""
QUESTION:
Create a function named `rearrange_characters` that takes a string of alphabetic characters and spaces as input and returns a new string where the characters in each word are shifted one position forward in the alphabet, while maintaining the original word order and case. The shift wraps around from 'z' to 'a' and from 'Z' to 'A'. Do not use any built-in string manipulation functions or libraries.
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