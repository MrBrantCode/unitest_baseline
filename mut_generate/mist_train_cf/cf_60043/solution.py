"""
QUESTION:
Design a function named `count_common_characters` that takes two strings `str1` and `str2` as input, counts the occurrences of common characters in both strings, and returns the total count. The function should count the minimum occurrence of each common character in both strings.
"""

def count_common_characters(str1, str2):
    # creating a set of unique characters for each string
    str1_set = set(str1)
    str2_set = set(str2)
    
    # getting intersection of two sets, which is common characters
    common_chars_set = str1_set & str2_set

    # counting each common character's occurrence in both strings and summing them
    common_chars_count = sum(min(str1.count(char), str2.count(char)) for char in common_chars_set)
    
    return common_chars_count