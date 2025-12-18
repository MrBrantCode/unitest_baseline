"""
QUESTION:
Time Limit: 8 sec / Memory Limit: 64 MB





Example

Input

eggchickenegg


Output

egg
"""

def determine_origin(s: str) -> str:
    i = c = p = 0
    b = ''
    r = ''
    
    while i < len(s):
        if s[i] == b:
            if c > p:
                r = b
                p = c
            c = 0
        b = s[i]
        i += [3, 7][s[i] == 'c']
        c += 1
    
    if c > p:
        r = b
    
    return ['chicken', 'egg'][r == 'e']