"""
QUESTION:
Write a function named `is_one_away` that takes two strings `str1` and `str2` as input and determines if `str1` is one character away from `str2`. The function should be case sensitive, handle whitespace, and return False if the difference in length between the two strings is greater than 1.
"""

def is_one_away(str1, str2):
    # Remove whitespace and convert to lowercase
    str1 = str1.strip().lower()
    str2 = str2.strip().lower()
    
    # Check if the difference in length is greater than 1
    if abs(len(str1) - len(str2)) > 1:
        return False
    
    # If the strings have the same length, check if they differ in exactly one character
    if len(str1) == len(str2):
        diff_count = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                diff_count += 1
                if diff_count > 1:
                    return False
        return True
    
    # If the strings have a length difference of 1, check if they can be made equal by removing one character
    elif abs(len(str1) - len(str2)) == 1:
        longer_str = max(str1, str2, key=len)
        shorter_str = min(str1, str2, key=len)
        
        i = j = 0
        while i < len(longer_str) and j < len(shorter_str):
            if longer_str[i] != shorter_str[j]:
                i += 1
                if i - j > 1:
                    return False
            else:
                i += 1
                j += 1
        return True
    
    # If the strings have the same length, but differ by more than one character
    else:
        return False