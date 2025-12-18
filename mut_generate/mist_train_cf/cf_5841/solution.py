"""
QUESTION:
Write a function `find_string` that takes a list of strings `list_strings` and a target string `target_string` as input. The function should return the index of the first occurrence of the target string in the list. If the target string is not found, return the index of the first string that starts with the same letter as the target string. If no such string is found, return the index of the first string that contains a vowel. If no string meets these conditions, return -1.
"""

def find_string(list_strings, target_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i, string in enumerate(list_strings):
        if string == target_string:
            return i
        elif string[0] == target_string[0] and string != target_string:
            return i
    for i, string in enumerate(list_strings):
        for vowel in vowels:
            if vowel in string.lower():
                return i
    return -1