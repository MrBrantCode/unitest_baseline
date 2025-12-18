"""
QUESTION:
Write a function `check_end_string(str1, str2)` that takes two strings as input and returns True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences. The function should have a time complexity of O(n), where n is the length of the longer string, and a space complexity of O(1). The input strings can contain alphabetic characters only, and the length of the input strings will not exceed 10^4 characters.
"""

def check_end_string(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    len_str1 = len(str1)
    len_str2 = len(str2)
    
    if len_str1 < len_str2:
        str1, str2 = str2, str1
        
    if str1[-len_str2:] == str2:
        return True
    else:
        return False