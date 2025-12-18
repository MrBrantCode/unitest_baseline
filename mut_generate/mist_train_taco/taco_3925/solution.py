"""
QUESTION:
Sometimes it is hard to prepare tests for programming problems. Now Bob is preparing tests to new problem about strings — input data to his problem is one string. Bob has 3 wrong solutions to this problem. The first gives the wrong answer if the input data contains the substring s1, the second enters an infinite loop if the input data contains the substring s2, and the third requires too much memory if the input data contains the substring s3. Bob wants these solutions to fail single test. What is the minimal length of test, which couldn't be passed by all three Bob's solutions?

Input

There are exactly 3 lines in the input data. The i-th line contains string si. All the strings are non-empty, consists of lowercase Latin letters, the length of each string doesn't exceed 105.

Output

Output one number — what is minimal length of the string, containing s1, s2 and s3 as substrings.

Examples

Input

ab
bc
cd


Output

4


Input

abacaba
abaaba
x


Output

11
"""

from itertools import permutations
from functools import lru_cache

@lru_cache(None)
def findPattern(s):
    slen = len(s)
    p = [0] * slen
    ci = 0
    for i in range(1, slen):
        if s[ci] == s[i]:
            ci += 1
            p[i] = ci
        else:
            while ci:
                ci = p[ci - 1]
                if s[ci] == s[i]:
                    ci += 1
                    p[i] = ci
                    break
    return tuple(p)

@lru_cache(None)
def searchPattern(s, ps, p):
    slen = len(s)
    plen = len(p)
    smatch = [0] * slen
    pi = 0
    for i in range(slen):
        if s[i] == ps[pi]:
            pi += 1
            smatch[i] = pi
        else:
            while pi:
                pi = p[pi - 1]
                if s[i] == ps[pi]:
                    pi += 1
                    smatch[i] = pi
                    break
        if pi == plen:
            pi = p[pi - 1]
    return smatch

def calcLength(a, b, c):
    pb = findPattern(b)
    amatchb = searchPattern(a, b, pb)
    if len(b) not in amatchb:
        ab = a[:max(0, len(a) - amatchb[-1])] + b
    else:
        ab = a
    pc = findPattern(c)
    abmatchc = searchPattern(ab, c, pc)
    return max(0, len(ab) - abmatchc[-1]) + len(c) if len(c) not in abmatchc else len(ab)

def minimal_test_length(s1, s2, s3):
    ans = float('inf')
    s = [s1, s2, s3]
    for (ai, bi, ci) in permutations(list(range(3)), 3):
        ans = min(ans, calcLength(s[ai], s[bi], s[ci]))
    return ans