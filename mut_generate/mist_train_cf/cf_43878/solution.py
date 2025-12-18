"""
QUESTION:
Write a function `is_anagram(str1, str2)` that takes two strings as input and returns True if they are anagrams of each other, ignoring spaces and case differences, and False otherwise.
"""

def is_anagram(str1, str2):
    str1_list = list(str1.replace(" ","").lower())
    str1_list.sort()
    str2_list = list(str2.replace(" ","").lower())
    str2_list.sort()

    return (str1_list == str2_list)