"""
QUESTION:
Create a function `merge_strings(str1, str2)` that merges two alphanumeric strings character by character to form a new string. If the strings are not of the same length, the extra characters from the longer string should follow sequentially after the intertwined section. The function should return the merged string.
"""

def merge_strings(str1, str2):
    min_length = min(len(str1), len(str2))
    merged = ''.join([str1[i] + str2[i] for i in range(min_length)])
    if len(str1) > min_length:
        merged += str1[min_length:]
    elif len(str2) > min_length:
        merged += str2[min_length:]
    return merged