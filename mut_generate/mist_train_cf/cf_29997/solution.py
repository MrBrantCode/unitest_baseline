"""
QUESTION:
Write a function `count_characters(s: str) -> dict` that takes a string `s` as input and returns a dictionary containing the frequency of each alphabetic character in the string, ignoring case sensitivity and non-alphabetic characters. The keys of the dictionary should be lowercase letters, and the values should be the count of each character in the input string.
"""

def count_characters(s: str) -> dict:
    s = s.lower()
    char_freq = {}
    
    for char in s:
        if char.isalpha():
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1
                
    return char_freq