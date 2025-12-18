"""
QUESTION:
Create a function called `remove_adjacent_duplicates` that takes a string `s` as input. The function should remove all adjacent duplicate characters from the string and return the resulting string.
"""

def remove_adjacent_duplicates(s):
    s = list(s)
    n = len(s)
    i = 0
    while i < n - 1:
        if s[i] == s[i+1]:
            s.pop(i)
            s.pop(i) 
            n -= 2
            if i != 0:
                i -= 1 
        else:
            i += 1
    return "".join(s)