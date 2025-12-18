"""
QUESTION:
Write a function `check_anagram(string1, string2)` to determine if two input strings are anagrams of each other. The function should have a time complexity of O(n), where n is the length of the input strings, and should not use any built-in or library functions. The function should return `True` if the strings are anagrams and `False` otherwise.
"""

def check_anagram(string1, string2):
    if len(string1) != len(string2):
        return False
    
    count1 = [0]*256
    count2 = [0]*256

    for i in range(len(string1)):
        count1[ord(string1[i])] += 1
        count2[ord(string2[i])] += 1

    for i in range(256):
        if count1[i] != count2[i]:
            return False

    return True