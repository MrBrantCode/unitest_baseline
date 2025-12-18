"""
QUESTION:
Write a function `is_happy(s)` that takes a string `s` as input and returns `True` if the string is happy and `False` otherwise. A string is considered happy if its length is no less than 3, each set of 3 sequential characters are unique, and every distinct character occurs at least twice.
"""

def entrance(s):
    if len(s) < 3:
        return False

    char_count = {}
    for i in range(len(s) - 2):
        triplet = s[i:i+3]
        if len(set(triplet)) != 3:
            return False
        
        for char in set(triplet):
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    for count in char_count.values():
        if count < 2:
            return False

    return True