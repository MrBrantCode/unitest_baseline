"""
QUESTION:
Write a function `char_word_frequency(s)` that takes a string `s` as input, calculates the frequency of each character and word in the string (case-insensitive, ignoring spaces, punctuation, and special symbols), and returns the frequency dictionaries. The function should handle case insensitivity and word frequency count.
"""

def char_word_frequency(s):
    s = s.lower()  
    words = ''.join(e for e in s if e.isalnum() or e.isspace()).split()
    chars = ''.join(words)
    
    char_dict = {}  
    for char in chars:
        if char.isalpha():
            char_dict[char] = char_dict.get(char, 0) + 1 

    word_dict = {}
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1 

    return char_dict, word_dict