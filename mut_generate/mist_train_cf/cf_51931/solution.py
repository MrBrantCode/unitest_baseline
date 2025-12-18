"""
QUESTION:
Create a function `find_substring(string_1, string_2)` that determines if `string_2` is a substring of `string_1` without using in-built substring functions or regular expressions. The function should return the starting index of `string_2` within `string_1` if it exists, otherwise return -1.
"""

def find_substring(string_1, string_2):
    len_1 = len(string_1)
    len_2 = len(string_2)

    if len_1 < len_2:
        return -1

    for i in range(len_1 - len_2 + 1):
        j = 0
        while(j < len_2):
            if string_1[i + j] != string_2[j]:
                break
            j += 1

        if j == len_2:
            return i

    return -1