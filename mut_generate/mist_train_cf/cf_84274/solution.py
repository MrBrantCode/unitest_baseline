"""
QUESTION:
Develop a function `first_unique_char(s)` that locates the first unique alphanumeric character in a given text sequence `s` and returns the character along with its positional index. The function should handle string inputs of variable lengths and must not use Python's built-in functions or libraries. If no unique character is found, return -1.
"""

def first_unique_char(s):
    frequency = {}
    for i in range(len(s)):  
        if not s[i] in frequency:
            frequency[s[i]] = [1, i]    
        else:
            frequency[s[i]][0] += 1    
    pos = len(s)    
    for v in frequency.values():
        if v[0] == 1:
            pos = min(pos, v[1])  
    if pos == len(s):    
        return -1
    else:   
        return s[pos], pos