"""
QUESTION:
Write a function `check_anagram(str1, str2)` that checks if two given strings are anagrams of each other without using any built-in functions. The function should be case-insensitive, ignore spaces and punctuation, and return True if the strings are anagrams, False otherwise.
"""

def check_anagram(str1, str2):
    str1 = ''.join(filter(str.isalpha, str1)).lower()
    str2 = ''.join(filter(str.isalpha, str2)).lower()

    if len(str1) != len(str2):
        return False
    
    counter1 = [0]*26
    counter2 = [0]*26

    for char in str1:
        pos = ord(char) - ord('a')
        counter1[pos] += 1

    for char in str2:
        pos = ord(char) - ord('a')
        counter2[pos] += 1
    
    return counter1 == counter2