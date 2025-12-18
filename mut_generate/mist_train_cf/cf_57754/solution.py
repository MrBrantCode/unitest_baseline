"""
QUESTION:
Create a function `cycpattern_check(a, b)` that checks whether the second string `b` or its rotations are substrings of the first string `a`. If not, determine if `b` can become a substring of `a` with the following restrictions:

- Only a limited number of letter swaps with adjacent letters are allowed (limited to 3).
- A certain character from `b` can only be replaced once.

The function should return `True` if `b` can be a substring of `a` under these conditions, and `False` otherwise.
"""

def cycpattern_check(a, b):
    def check(s1, s2):  
        counter = sum(abs(s1.count(c) - s2.count(c)) for c in set(s1 + s2))
        return counter <= 6  

    def rotate(s):  
        return s[-1] + s[:-1]

    ab = a + b  
    for _ in range(len(a)):
        for i in range(len(ab) - len(b) + 1):  
            window = ab[i:i+len(b)]
            if check(window, b):
                return True
        ab = rotate(ab)
    return False