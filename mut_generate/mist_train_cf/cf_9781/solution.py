"""
QUESTION:
Write a function `compare_strings` that takes two lowercase alphabet strings `str1` and `str2` as input, each with a maximum length of 100 characters. The function should return the lexicographically greater string. If the strings are equal, return the message "Both strings are equal."
"""

def compare_strings(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    
    for i in range(min(n1, n2)):
        if str1[i] != str2[i]:
            if ord(str1[i]) > ord(str2[i]):
                return str1
            else:
                return str2
    
    if n1 > n2:
        return str1
    elif n2 > n1:
        return str2
    else:
        return "Both strings are equal"