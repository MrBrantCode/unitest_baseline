"""
QUESTION:
Write a function `is_anagram` that takes two strings as arguments and returns `True` if they are anagrams of each other, and `False` otherwise. The function should be case-insensitive, ignore leading and trailing whitespace, and remove special characters and whitespace from the strings. If the strings are of different lengths after preprocessing, the function should return `False`. The time complexity should be O(n + m), where n and m are the lengths of the input strings, and the space complexity should be O(k), where k is the number of unique characters in both strings combined.
"""

def is_anagram(str1, str2):
    # Strip leading and trailing whitespace
    str1 = str1.strip()
    str2 = str2.strip()
    
    # Convert both strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()
    
    # Remove special characters and whitespace from both strings
    str1 = ''.join(c for c in str1 if c.isalnum())
    str2 = ''.join(c for c in str2 if c.isalnum())
    
    if len(str1) != len(str2):
        return False
    
    str1_dict = {}
    for char in str1:
        if char in str1_dict:
            str1_dict[char] += 1
        else:
            str1_dict[char] = 1

    for char in str2:
        if char not in str1_dict:
            return False
        else:
            str1_dict[char] -= 1
            if str1_dict[char] == 0:
                del str1_dict[char]

    if len(str1_dict) == 0:
        return True
    else:
        return False