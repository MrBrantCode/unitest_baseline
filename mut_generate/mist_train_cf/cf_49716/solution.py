"""
QUESTION:
Write a function called `can_sort(s, t)` that determines if string `s` can be transformed into string `t` using a substring sort operation. The function should return `True` if it's possible to transform `s` into `t`, and `False` otherwise. The lengths of `s` and `t` are equal, and both strings contain only digits ranging from '0' to '9'.
"""

def can_sort(s, t):
    # frequency counts
    counts_s, counts_t = [0] * 10, [0] * 10
    for ch_s, ch_t in zip(s, t):
        # generate character frequency counts
        counts_s[ord(ch_s)-ord('0')] += 1
        counts_t[ord(ch_t)-ord('0')] += 1
        # if at this point, any character in t has more
        # occurrences than in s, return False
        if any(a < b for a, b in zip(counts_s, counts_t)):
            return False
    # if we reached here it means we can sort s to get t
    return True