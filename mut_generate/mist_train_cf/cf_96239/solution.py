"""
QUESTION:
Create a function called `is_anagram` that takes two strings `str1` and `str2` as input and returns a boolean indicating whether they are anagrams of each other. The function should have a time complexity of O(n^2), where n is the length of the strings, and a space complexity of O(n).
"""

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    str1_list = list(str1)
    str2_list = list(str2)
    str1_list.sort()
    str2_list.sort()
    for i in range(len(str1_list)):
        if str1_list[i] != str2_list[i]:
            return False
    return True