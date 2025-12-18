"""
QUESTION:
Implement the function `canConvert(str1, str2, k, s)` that takes two strings `str1` and `str2` of the same length, and two integers `k` and `s` as input. The function should return `True` if `str1` can be transformed into `str2` by doing zero or more conversions and character swaps, and `False` otherwise.

In one conversion, you can convert all occurrences of one character in `str1` to any other lowercase English character, with a maximum of `k` conversions allowed. In one swap, you can swap the positions of any two characters in `str1`, with a maximum of `s` swaps allowed.
"""

def canConvert(str1, str2, k, s):
    count1, count2 = [0]*26, [0]*26
    for i in range(len(str1)):
        count1[ord(str1[i]) - ord('a')] += 1
        count2[ord(str2[i]) - ord('a')] += 1
    for i in range(26):
        if count2[i] > count1[i]:
            return False
    changes, swaps = set(), 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if str1[i] in changes or swaps == s:
                if str1[i] in str1[i+1:]:
                    swaps += 1
                elif len(changes) < k:
                    changes.add(str1[i])
                else:
                    return False
    return True