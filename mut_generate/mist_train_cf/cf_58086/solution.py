"""
QUESTION:
Write a function `are_anagrams` that takes two lists of strings as input and returns a list of boolean values indicating whether the corresponding strings in each list are anagrams of each other, ignoring case and non-alphanumeric characters. The function should be efficient for large input lists.
"""

def are_anagrams(str_set1, str_set2):
    result = []
    for str1, str2 in zip(str_set1, str_set2):
        sorted_str1 = ''.join(sorted(c for c in str1.lower() if c.isalnum()))
        sorted_str2 = ''.join(sorted(c for c in str2.lower() if c.isalnum()))
        result.append(sorted_str1 == sorted_str2)
    return result