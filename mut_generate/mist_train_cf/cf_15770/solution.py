"""
QUESTION:
Create a function `permuteUnique(s)` that generates all unique permutations of a given string `s` in lexicographic order, considering that the string may contain duplicate characters. The function should return a list of strings where each string is a permutation of the input string.
"""

def permuteUnique(s):
    def backtrack(start):
        if start == len(s) - 1:
            result.append(''.join(s))
            return
        seen = set()
        for i in range(start, len(s)):
            if s[i] in seen:
                continue
            seen.add(s[i])
            s[start], s[i] = s[i], s[start]
            backtrack(start + 1)
            s[start], s[i] = s[i], s[start]

    s = sorted(s)
    result = []
    backtrack(0)
    return result