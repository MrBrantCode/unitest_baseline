"""
QUESTION:
Implement a function `check_end_strings(str1, str2)` that determines if either of the input strings appears at the very end of the other string, ignoring upper/lower case differences. The function should have a time complexity of O(n), where n is the length of the longer string, and a space complexity of O(1). The input strings can contain only alphabetic characters and their lengths will not exceed 10^4 characters. The solution should not use any built-in string matching functions or libraries.
"""

def check_end_strings(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    return str1.endswith(str2) or str2.endswith(str1)