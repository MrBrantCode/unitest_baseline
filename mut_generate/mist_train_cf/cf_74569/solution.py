"""
QUESTION:
Given a string `s` containing only lowercase English letters and with a length between 1 and 4 * 10^5, write a function named `lastSubstring` that returns the last substring of `s` in lexicographical order along with its starting index. The function should be able to handle strings of the given length efficiently.
"""

def lastSubstring(s: str):
    n = len(s)
    max_ch = max(s)
    indices = [i for i, ch in enumerate(s) if ch == max_ch]
    substrings = [s[i:] for i in indices]
    max_substring = max(substrings)
    return (max_substring, s.rfind(max_substring))