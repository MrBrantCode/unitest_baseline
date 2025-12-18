"""
QUESTION:
Create a function called `rotateString(s, r)` that takes two parameters: a string `s` and an integer `r`. The function should rotate the characters in `s` circularly by `r` positions. If `r` is greater than the length of `s`, the function should return the reverse of `s`. The function cannot use any built-in string or array conversion methods, and it should only use basic operations such as concatenation and iteration.
"""

def rotateString(s, r):
    result = ''
    if r > len(s):
        for i in range(len(s), 0, -1):
            result += s[i-1]
    else:
        for j in range(r, 0, -1):
            result += s[-j]
        for k in range(0, len(s)-r):
            result +=s[k]
    return result