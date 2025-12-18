"""
QUESTION:
Write a function `repeatedSubstringPattern(s: str)` that determines if a given string `s` can be constructed by taking a substring of it and appending multiple copies of the substring together, where the substring can overlap with itself in the repeated pattern. The function should return a boolean value indicating whether such a pattern exists.

The string `s` consists of lowercase English letters and its length is between 1 and 10^4.
"""

def repeatedSubstringPattern(s: str) -> bool:
    def compute_LPS_array(s: str):
        lps = [0] * len(s)
        length = 0
        i = 1
        while i < len(s):
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length-1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    lps = compute_LPS_array(s)
    lps_last_val = lps[-1]
    len_s = len(s)
    return lps_last_val > 0 and len_s % (len_s - lps_last_val) == 0