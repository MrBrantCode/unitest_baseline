"""
QUESTION:
Write a function `checkInclusion(s1: str, s2: str) -> bool` that returns `True` if `s2` contains a permutation of `s1` as a substring. Both `s1` and `s2` are lowercase strings. The length of both strings is between 1 and 10,000.
"""

def checkInclusion(s1: str, s2: str) -> bool:
    from collections import Counter
    length_s1 = len(s1)
    length_s2 = len(s2)
    if length_s1 > length_s2:
        return False
    count_s1 = Counter(s1)
    count_s2 = Counter()
    for i in range(length_s2):
        count_s2[s2[i]] += 1
        if i >= length_s1:
            if count_s2[s2[i - length_s1]] == 1:
                del count_s2[s2[i - length_s1]]
            else:
                count_s2[s2[i - length_s1]] -= 1
        if count_s1 == count_s2:
            return True
    return False