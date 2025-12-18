"""
QUESTION:
Write a function `split_stream(s)` that splits a given hexadecimal string `s` into a list of 4-character strings, starting from the first occurrence of '0100FF18' in the string. If '0100FF18' is not found in the string, the function should return an empty list. The input string `s` only contains hexadecimal characters (0-9, A-F).
"""

def split_stream(s):
    if '0100FF18' not in s:
        return []
    s = s.split('0100FF18')[1]  
    return [s[i:i+4] for i in range(0, len(s), 4)]