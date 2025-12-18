"""
QUESTION:
Write a function `isIsomorphic(string1, string2)` that determines if two input strings are isomorphic. Two strings are isomorphic if there is a one-to-one mapping possible for every character of `string1` to every character of `string2` while preserving the order. The function should not use any built-in Python functions. The strings are isomorphic if and only if the function returns `True`. The function must handle cases where the strings are of different lengths and return `False` in such cases.
"""

def isIsomorphic(string1, string2):
    if len(string1) != len(string2): 
        return False
    s1 = {} 
    s2 = {} 
    for i in range(len(string1)):
        if string1[i] in s1:
            if s1[string1[i]] != string2[i]: 
                return False
        else:
            if string2[i] in s2: 
                return False
            s1[string1[i]] = string2[i]
            s2[string2[i]] = string1[i] 
    return True