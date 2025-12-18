"""
QUESTION:
Write a function `check_palindrome(str1, str2)` that determines whether two given strings can be palindromically rearranged into each other without using any built-in Python functions. The function should return `True` if the strings can be palindromically rearranged and `False` otherwise. The input strings are case-sensitive and only contain lowercase letters.
"""

def check_palindrome(str1, str2):
    frequency_count1 = [0]*26
    frequency_count2 = [0]*26

    for i in range(len(str1)):
        frequency_count1[ord(str1[i]) - ord('a')] += 1

    for i in range(len(str2)):
        frequency_count2[ord(str2[i]) - ord('a')] += 1

    for i in range(26):
        if frequency_count1[i] != frequency_count2[i]:
            return False
      
    return True