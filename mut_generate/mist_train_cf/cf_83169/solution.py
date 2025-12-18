"""
QUESTION:
Implement a function `customSortString(S, T)` where `S` and `T` are strings composed solely of lowercase alphabets, `S` has a maximum length of 26, and no alphabet is duplicated in `S`. The function should return any permutation of `T` that maintains the order of characters as in `S`, with characters not present in `S` appended at the end.
"""

import collections

def customSortString(S, T):
    count = collections.Counter(T)  
    ans = []
    for s in S:  
        ans.append(s * count[s])  
        count[s] = 0  
    for c in count:
        ans.append(c * count[c])  
    return "".join(ans)