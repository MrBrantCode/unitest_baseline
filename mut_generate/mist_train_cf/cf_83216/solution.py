"""
QUESTION:
Write a function `replace_vowels(s)` that takes a string `s` as input and returns a new string where all vowels are replaced with the subsequent alphabetical character. The function should handle both lowercase and uppercase vowels, as well as special characters, and should be efficient enough to handle large strings.
"""

def replace_vowels(s):
    s = list(s)
    for i in range(len(s)):
        if s[i].lower() in 'aeiou':
            s[i] = chr(ord(s[i])+1)
    return ''.join(s)