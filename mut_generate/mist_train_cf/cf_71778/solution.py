"""
QUESTION:
Construct a function named `find_z_followed_by_2y` that takes a string `s` as input and returns the index of the first occurrence of a 'z' immediately followed by at least two 'y's, disregarding letter casing. If no such pattern exists, return -1.
"""

def find_z_followed_by_2y(s):
    s = s.lower()
    for index in range(len(s) - 2):
        if s[index] == 'z' and s[index+1] == 'y' and s[index+2] == 'y':
            return index
    return -1