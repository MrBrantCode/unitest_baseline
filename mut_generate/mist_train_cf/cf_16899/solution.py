"""
QUESTION:
Write a function named `delete_occurrences` that takes two strings `str1` and `str2` as input and returns a string with all occurrences of `str2` deleted from `str1`. The function should have a time complexity of O(n), where n is the length of `str1`, and a space complexity of O(1). The input strings can contain any printable ASCII characters and can be up to 10^6 characters long. The function should not use any built-in string manipulation functions or regular expressions, and should be implemented using a single pass algorithm without recursion.
"""

def delete_occurrences(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    if len2 == 0:
        return str1

    i = 0
    j = 0

    while i < len1:
        if str1[i] == str2[j]:
            i += 1
            j += 1

            if j == len2:
                str1 = str1[:i-len2] + str1[i:]
                len1 -= len2
                i -= len2
                j = 0
        else:
            j = 0
            i += 1

    return str1