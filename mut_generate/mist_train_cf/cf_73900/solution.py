"""
QUESTION:
Write a function `isScramble(s1: str, s2: str) -> bool` that determines whether string `s2` is a scrambled version of string `s1`. The function should return `true` if `s2` is a scrambled version of `s1`, and `false` otherwise. The lengths of `s1` and `s2` are equal and between 1 and 30, and both strings are composed of lower-case English alphabets.
"""

def isScramble(s1: str, s2: str) -> bool:
    memo = {}

    def helper(s1, s2):
        if (s1, s2) in memo:
            return memo[s1, s2]
        if s1 == s2:
            memo[s1, s2] = True
            return True
        if sorted(s1) != sorted(s2):
            memo[s1, s2] = False
            return False
        L = len(s1)
        for i in range(1, L):
            if (helper(s1[:i], s2[:i]) and helper(s1[i:], s2[i:])) or \
                    (helper(s1[:i], s2[-i:]) and helper(s1[i:], s2[:-i])):
                memo[s1, s2] = True
                return True
        memo[s1, s2] = False
        return False

    return helper(s1, s2)