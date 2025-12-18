"""
QUESTION:
Arrange the letters in a given string in alphabetical order while preserving the original positions of non-alphabetic characters, such as numbers and special characters. The function should handle both upper and lower case letters, and it should not be case sensitive when comparing letters. Design the function `sort_string(s)` where `s` is the input string.
"""

def sort_string(s):
    char_list = [c for c in s if c.isalpha()]
    char_list.sort(key=str.lower)
    
    sorted_s = ""
    char_index = 0
    for i in range(len(s)):
        if s[i].isalpha():
            sorted_s += char_list[char_index]
            char_index += 1
        else:
            sorted_s += s[i]
    return sorted_s