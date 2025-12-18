"""
QUESTION:
Write a function `compare_strings(str1, str2)` that determines if two input strings are equal while considering case sensitivity and whitespace, but ignoring punctuation marks. The solution should not use any built-in string comparison functions or methods and should have a time complexity of O(n), where n is the length of the longer string.
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