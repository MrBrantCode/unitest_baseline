"""
QUESTION:
Write a function `get_permutations(string)` to generate all unique permutations of the given string, considering that the string may contain duplicate characters. The function should correctly handle an empty string input.
"""

def get_permutations(string):
    if len(string) == 0:
        return []

    permutations = set()  
    def backtrack(combination, remaining):
        if len(remaining) == 0:
            permutations.add(combination)
            return

        for i in range(len(remaining)):
            backtrack(combination + remaining[i], remaining[:i] + remaining[i+1:])

    backtrack("", string)
    return [''.join(p) for p in permutations]