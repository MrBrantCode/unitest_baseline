"""
QUESTION:
Write a function `reverse_string(s)` that takes a string `s` as input and returns a new string where all the letters are reversed, while keeping the positions of non-letter characters (such as spaces and punctuation) unchanged. The function should work with any input string and should not modify the original string.
"""

def reverse_string(s):
    s = list(s)
    letters = [i for i in s if i.isalpha()]
    letters.reverse()
    
    for i in range(len(s)):
        if s[i].isalpha():
            s[i] = letters.pop(0)
    return ''.join(s)