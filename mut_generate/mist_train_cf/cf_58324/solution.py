"""
QUESTION:
Create a function `modified_string` that takes two strings `str1` and `str2`, and an integer `n` as input. The function should return a new string that takes the first three characters of `str1` and `str2`, and inserts `str2` at the `n`-th position of `str1`. If `n` exceeds the length of `str1`, return the message "Impractical index value".
"""

def modified_string(str1: str, str2: str, n: int) -> str:
    if n > len(str1):
        return "Impractical index value"
    str1 = str1[:3] + str1[3:]
    str2 = str2[:3]
    return str1[:n] + str2 + str1[n:]