"""
QUESTION:
Write a function `compare_consonants(str1, str2)` that compares two strings lexicographically, considering only English consonants (both lowercase and uppercase). The function should return a string indicating which of the input strings is lexicographically greater or whether they are equal.
"""

def compare_consonants(str1, str2):
    consonants = "bcdfghjklmnpqrstvwxyz"
    str1 = "".join(char for char in str1.lower() if char in consonants)
    str2 = "".join(char for char in str2.lower() if char in consonants)
    
    if str1 > str2:
        return "String 1 is lexicographically greater"
    elif str1 < str2:
        return "String 2 is lexicographically greater"
    else:
        return "Strings are equal"