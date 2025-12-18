"""
QUESTION:
Write a function `compare_strings` that takes two strings as input and returns a boolean indicating whether the strings are equal, ignoring punctuation marks but considering case and whitespace. The function should not use any built-in string comparison functions or methods and should have a time complexity of O(n), where n is the length of the longer string.
"""

def compare_strings(str1, str2):
    def ignore_punctuation(ch):
        if ch.isalpha() or ch.isspace():
            return ch
        return ''

    i, j = 0, 0
    while i < len(str1) and j < len(str2):
        ch1 = ignore_punctuation(str1[i])
        ch2 = ignore_punctuation(str2[j])
        
        if ch1 != ch2:
            return False
        
        i += 1
        j += 1
    
    return i == len(str1) and j == len(str2)