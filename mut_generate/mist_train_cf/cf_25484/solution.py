"""
QUESTION:
Create a function named `is_anagram` that takes two strings as input and returns a boolean value indicating whether the two strings are anagrams. The function should be case-insensitive, meaning it treats uppercase and lowercase letters as the same. The function should return False if the strings are not anagrams and True if they are.
"""

def is_anagram(str1, str2): 
    # convert the strings to lowercase 
    str1 = str1.lower() 
    str2 = str2.lower() 

    # sorting both the strings 
    s1 = sorted(str1) 
    s2 = sorted(str2) 

    if len(s1) != len(s2): 
        return False

    # compare character by character 
    for i in range(len(s1)): 
        if s1[i] != s2[i]: 
            return False
    return True