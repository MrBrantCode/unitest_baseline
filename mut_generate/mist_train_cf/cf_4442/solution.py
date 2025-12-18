"""
QUESTION:
Write a function `are_anagrams` that takes two strings of lowercase letters as input and returns `True` if they are anagrams of each other and `False` otherwise. The function must have a time complexity of O(n), where n is the length of the input strings, and cannot use built-in functions or libraries for sorting or counting characters, or any additional data structures like dictionaries, lists, or sets.
"""

def are_anagrams(str1, str2):
    if len(str1) != len(str2):  
        return False

    char_counts = [0] * 26  

    for i in range(len(str1)):
        char_counts[ord(str1[i]) - ord('a')] += 1
        char_counts[ord(str2[i]) - ord('a')] -= 1

    for count in char_counts:
        if count != 0:  
            return False

    return True