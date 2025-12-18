"""
QUESTION:
Create a function `permute(s)` that generates all possible permutations of a given string `s`, where `s` may contain duplicate characters, and returns them as a list of strings. The function should ensure that the returned permutations are unique, without duplicates.
"""

def permute(s):
    result = []
    visited = [False] * len(s)
    permuteHelper(s, "", visited, result)
    return result

def permuteHelper(s, current, visited, result):
    if len(current) == len(s):
        result.append(current)
        return

    for i in range(len(s)):
        if visited[i]:
            continue
        visited[i] = True
        permuteHelper(s, current + s[i], visited, result)
        visited[i] = False