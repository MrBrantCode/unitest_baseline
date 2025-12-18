"""
QUESTION:
Create a function `check_transpose_anagram(s)` that takes a string `s` as input. The function should return `True` if the reverse of `s` is an anagram of `s`, and `False` otherwise. The function should assume that the input string contains only lowercase letters and does not contain spaces or punctuation.
"""

def is_anagram_after_reversal(s):
    #get transpose string by reversing the input string
    t = s[::-1]
    
    #convert string to list and sort them, then compare
    return sorted(list(s)) == sorted(list(t))