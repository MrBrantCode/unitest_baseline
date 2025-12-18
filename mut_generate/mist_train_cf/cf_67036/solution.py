"""
QUESTION:
Compare two input strings based on their lexicographical order and return a comparison result.

The function, `compare_strings`, should take two required parameters `str1` and `str2` (the input strings to be compared) and one optional parameter `case_sensitive` (a boolean indicating whether the comparison is case sensitive, defaulting to `True`).

The function should return an integer: 0 if `str1` and `str2` are equal, 1 if `str1` is greater than `str2`, and -1 if `str2` is greater than `str1`. Special characters and numbers should be treated differently than the English alphabet.
"""

def compare_strings(str1, str2, case_sensitive=True):
    if not case_sensitive:
        str1 = str1.lower()
        str2 = str2.lower()
    
    if str1 == str2:
        return 0
    elif str1 > str2:
        return 1
    else:
        return -1