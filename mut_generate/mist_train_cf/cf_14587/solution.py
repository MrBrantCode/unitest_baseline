"""
QUESTION:
Create a function 'findPattern' that takes two strings as parameters and returns 1 if the second string is a subsequence of the first string, otherwise 0. The function must be case-insensitive and handle Unicode characters and special characters. It should have a time complexity of O(n), where n is the length of the first string, and a space complexity of O(1), meaning it should not use any additional data structures.
"""

def findPattern(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    ptr1 = 0
    ptr2 = 0

    while ptr1 < len(str1) and ptr2 < len(str2):
        if str1[ptr1] == str2[ptr2]:
            ptr1 += 1
            ptr2 += 1
        else:
            ptr1 += 1

    if ptr2 == len(str2):
        return 1
    else:
        return 0