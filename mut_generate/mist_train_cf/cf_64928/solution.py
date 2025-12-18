"""
QUESTION:
Implement a function `check_anagrams(str1, str2)` that checks if two given strings are anagrams of each other without using built-in library functions or data structures, assuming the strings only contain lowercase English letters. The function should return a boolean value indicating whether the strings are anagrams or not.
"""

def check_anagrams(str1, str2):
    # If the lengths of both strings are not equal, return False
    if len(str1) != len(str2):
        return False

    count_arr1 = [0] * 26  # count array of 26 for 26 english characters
    count_arr2 = [0] * 26

    for i in range(len(str1)):
        count_arr1[ord(str1[i])-ord('a')] += 1
        count_arr2[ord(str2[i])-ord('a')] += 1

    for i in range(26):
        if count_arr1[i] != count_arr2[i]:
            return False

    return True