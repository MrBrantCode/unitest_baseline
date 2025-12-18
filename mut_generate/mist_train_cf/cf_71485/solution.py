"""
QUESTION:
Implement a function `is_isomorphic(str1, str2)` that checks whether two input strings are isomorphic without utilizing any predefined or inbuilt functions. Two strings are isomorphic if the characters in the first string can be replaced to get the second string, where each character in the first string maps to exactly one character in the second string and no character maps to multiple characters. The function should handle large strings efficiently, with lengths up to 10^4 characters, and account for potential special characters and numbers included in the string.
"""

def is_isomorphic(str1, str2):
    mapping = {}
    mapped = set()

    for i in range(len(str1)):
        if str1[i] not in mapping:
            if str2[i] in mapped:
                return False
            mapping[str1[i]] = str2[i]
            mapped.add(str2[i])
        elif mapping[str1[i]] != str2[i]:
            return False
    return True