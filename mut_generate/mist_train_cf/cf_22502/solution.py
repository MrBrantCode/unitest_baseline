"""
QUESTION:
Write a function `compare_strings` that compares two strings lexicographically in a case-insensitive manner, ignoring any leading or trailing whitespace characters, and returns "bigger", "smaller", or "equal" accordingly. The input strings will only contain alphabets and their lengths will be between 1 and 100 (inclusive).
"""

def compare_strings(str1, str2):
    str1 = str1.strip().lower()
    str2 = str2.strip().lower()
    
    if str1 < str2:
        return "smaller"
    elif str1 > str2:
        return "bigger"
    else:
        return "equal"