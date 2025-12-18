"""
QUESTION:
Write a function named `is_subsequence` that takes two strings `str1` and `str2` as input and returns `True` if `str1` is a subsequence of `str2`, and `False` otherwise. A string is considered a subsequence of another if its characters appear in the same order, but not necessarily contiguously, in the other string.
"""

def is_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)

    j = 0    # This index is used for str1 

    # Traverse str2 and str1, and compare current character  
    # of str2 with first unmatched character of str1, if matched then move 
    # ahead in str1
    for i in range(n):
        if j == m:
            break
        # If current character of str1 matches with the current character of str2
        if str1[j] == str2[i]: 
            j += 1    # move ahead in str1

    # If all characters of str1 were found in str2
    return j == m