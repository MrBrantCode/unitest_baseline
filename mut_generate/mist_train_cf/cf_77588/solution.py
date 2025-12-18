"""
QUESTION:
Given two equal-size strings `s` and `t`, and a third string `p` containing the only characters that can be used to replace characters in `t`, write a function `minSteps` that returns the minimum number of steps to make `t` an anagram of `s` using only characters from `p`. The replacement operation can only be performed on the characters of `t` that are at even indices, and the characters in `p` can only be used once for replacement. If it is not possible to make `t` an anagram of `s` using only characters from `p`, return -1. The function `minSteps` should take three parameters: `s`, `t`, and `p`, all of which are lower-case English letters and have a maximum length of 50000.
"""

def minSteps(s, t, p):
    from collections import Counter

    sCount = Counter(s)
    tCount = Counter(t)
    pCount = Counter(p)

    for i in range(0, len(t), 2):
        if t[i] in sCount and sCount[t[i]] > 0:
            if tCount[t[i]] > 1:
                tCount[t[i]] -= 1
            else:
                del tCount[t[i]]
            sCount[t[i]] -= 1
        elif t[i] in pCount and pCount[t[i]] > 0:
            if tCount[t[i]] > 1:
                tCount[t[i]] -= 1
            else:
                del tCount[t[i]]
            pCount[t[i]] -= 1
        else:
            return -1

    return sum((tCount & sCount).values())