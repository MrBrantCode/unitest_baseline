"""
QUESTION:
Write a function "is_happy" that takes a string "s" as a parameter. The string is considered "happy" if it meets the following conditions: 
- its length is at least three, 
- every sequence of three consecutive letters is unique, 
- each letter appears at minimum twice without them being successive. 
The function must use a dictionary to track the frequency of letter appearances and must not use string manipulation methods.
"""

def is_happy(s):
    if len(s) < 3:
        return False
    freq = {}
    for i in range(len(s)-1):
        if s[i] == s[i + 1]:
            return False
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    
    if s[-1] in freq:
        freq[s[-1]] += 1
    else:
        freq[s[-1]] = 1
    
    if max(list(freq.values())) < 2:
        return False
    
    seq = {}
    for i in range(len(s)-2):
        sequence = s[i:i+3]
        if sequence in seq:
            return False
        else:
            seq[sequence] = 1
    return True