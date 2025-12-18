"""
QUESTION:
Write a function `compare_strings(str1, str2)` to compare two strings and return the number of different characters in each string. The function should handle strings of different lengths and consider the extra characters in the longer string as different characters. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the longer string.
"""

def compare_strings(str1, str2):
    longer_str_len = max(len(str1), len(str2))
    shorter_str_len = min(len(str1), len(str2))
    
    count = longer_str_len - shorter_str_len
    
    for i in range(shorter_str_len):
        if ord(str1[i]) ^ ord(str2[i]) != 0:
            count += 1
    
    return count