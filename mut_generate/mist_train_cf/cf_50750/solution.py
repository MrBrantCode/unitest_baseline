"""
QUESTION:
Write a function named `is_ambigram` that takes a string of alphabetic and numeric characters as input and returns True if the string is an ambigram (i.e., it remains the same when its characters are reversed), considering some characters that look the same when upside down (e.g., '0', '1', '8', 'o', 'x', 'X'), and some that have a corresponding upside-down character (e.g., 'p' and 'q', 'b' and 'd'). The function should be case-insensitive and should handle strings of odd length, where the middle character must be symmetric.
"""

def is_ambigram(text):
    text = text.lower() 
    symmetric_chars = 'ahimotuvwx018'
    upside_down_chars = {'p':'q', 'q':'p', 'b':'d', 'd':'b', 'n':'u', 'u':'n'} 

    length = len(text)
    for i in range(length//2):
        if text[i] != text[length-i-1]:
            if text[i] not in upside_down_chars or text[length-i-1] != upside_down_chars[text[i]]:
                return False

    if length % 2 != 0:
        if text[length//2] not in symmetric_chars:
            return False

    return True