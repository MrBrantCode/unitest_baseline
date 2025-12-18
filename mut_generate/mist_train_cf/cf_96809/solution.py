"""
QUESTION:
Create a function called `are_anagrams` that takes two strings `str1` and `str2` as input. The function should determine whether `str1` and `str2` are anagrams without using built-in Python functions or libraries for string manipulation and sorting. The function should have a time complexity of O(n), where n is the length of the strings.
"""

def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    dict1 = {}
    dict2 = {}

    for ch in str1:
        if ch in dict1:
            dict1[ch] += 1
        else:
            dict1[ch] = 1

    for ch in str2:
        if ch in dict2:
            dict2[ch] += 1
        else:
            dict2[ch] = 1

    return dict1 == dict2