"""
QUESTION:
Write a function `licenseKeyFormatting` that takes a non-empty string `S` consisting of alphanumeric characters and dashes, and a positive integer `K`, and returns a formatted string where each group contains exactly `K` characters, except for the first group which could be shorter than `K` but still must contain at least one character, with all lowercase letters converted to uppercase and no two consecutive groups being the same. The length of string `S` will not exceed 12,000.
"""

def licenseKeyFormatting(S, K):
    """
    :type S: str
    :type K: int
    :rtype: str
    """
    S = S.replace("-","").upper()
    
    size = len(S)
    s1 = K if size%K==0 else size%K
    res = S[:s1]
    while s1<size:
        res += '-'+S[s1:s1+K]
        s1 += K
    return res