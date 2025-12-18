"""
QUESTION:
Create a function called `alter_string` that takes a string `s` as input and returns a new string containing only the characters from `s` that are at odd index positions. Use recursion to achieve this, and assume that index positions are 0-based (i.e., the first character is at index 0, which is even).
"""

def alter_string(s):
    if len(s)==0:
        return s
    else:
        return ("" if (len(s)-1)%2==0 else s[0]) + alter_string(s[1:])