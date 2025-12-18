"""
QUESTION:
Write a function `are_anagrams(str1, str2)` that checks if two input strings are anagrams of each other, considering case sensitivity and whitespace. The function should have a time complexity of O(n), where n is the size of the strings, to optimize for large strings.
"""

def are_anagrams(str1, str2):
    dict1 = {}
    dict2 = {}

    # count the number of occurrences of each character in str1
    for char in str1:
        if char in dict1:
            dict1[char] += 1
        else:
            dict1[char] = 1

    # count the number of occurrences of each character in str2
    for char in str2:
        if char in dict2:
            dict2[char] += 1
        else:
            dict2[char] = 1

    # if the dictionaries are not equal, 
    # it means the two strings are not anagrams of each other
    return dict1 == dict2