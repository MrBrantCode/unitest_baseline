"""
QUESTION:
Write a function named `permuteUnique` that takes a string `s` as input and returns all unique permutations of the string in lexicographic order. The input string may contain duplicate characters. The function should exclude duplicate permutations from the output.
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