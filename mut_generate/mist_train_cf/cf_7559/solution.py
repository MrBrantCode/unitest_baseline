"""
QUESTION:
Create a function `count_similar_characters` that takes two strings and returns the number of similar characters in both strings. The function should be case-sensitive and consider spaces as characters. The function should have a time complexity of O(n), where n is the length of the longer string, and should not use any built-in string comparison or similarity calculation methods, additional data structures, or recursion.
"""

def count_similar_characters(str1, str2):
    count = 0
    len1 = len(str1)
    len2 = len(str2)
    length = max(len1, len2)

    for i in range(length):
        if i < len1 and i < len2:
            if str1[i] == str2[i]:
                count += 1
        elif i < len1:
            count += 1
        elif i < len2:
            count += 1

    return count