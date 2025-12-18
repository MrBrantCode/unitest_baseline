"""
QUESTION:
Create a function `shortest_string(s1, s2, s3)` that takes three string parameters, removes all vowels (both uppercase and lowercase) from each string, and returns the string with the least characters after the vowels are removed. If two or more strings have the same least number of characters, return the first one from the left. Consider an empty string as shorter than any other strings, and if all strings are empty after removing vowels, return the first one. Vowels are 'a', 'e', 'i', 'o', 'u' in both lowercase and uppercase.
"""

def shortest_string(s1, s2, s3):
    s1 = ''.join([char for char in s1 if char not in 'aeiouAEIOU'])
    s2 = ''.join([char for char in s2 if char not in 'aeiouAEIOU'])
    s3 = ''.join([char for char in s3 if char not in 'aeiouAEIOU'])
    
    if len(s1) <= len(s2) and len(s1) <= len(s3):
        return s1
    elif len(s2) <= len(s3):
        return s2
    else:
        return s3