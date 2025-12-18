"""
QUESTION:
Write a function called `extract_middle_char` that takes a string as input and returns the middle character(s) as a new string. The string will have 1-100 lowercase letters. If the string length is odd, return the middle character; if the string length is even, return the two middle characters.
"""

def extract_middle_char(s):
    length = len(s)
    middle = length // 2
    if length % 2 == 0:
        return s[middle-1:middle+1]
    else:
        return s[middle]