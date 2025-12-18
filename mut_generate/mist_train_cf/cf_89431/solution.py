"""
QUESTION:
Write a function `check_end_strings(str1, str2)` that takes two strings as input and returns True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences. The solution should have a time complexity of O(n), where n is the length of the longer string, and a space complexity of O(1). 

The input strings can contain alphabetic characters only and their lengths will not exceed 10^4 characters. The solution should be implemented without using any built-in string matching functions or libraries.
"""

def check_end_strings(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    if str1[-len(str2):] == str2:
        return True

    if str2[-len(str1):] == str1:
        return True

    return False