"""
QUESTION:
Write a function `find_combinations(candidates, target)` that takes a list of integers `candidates` and an integer `target` as input, and returns all possible rearrangements of digits from the `candidates` list that sum up to `target`, where each number in `candidates` can be used multiple times and digit-level permutations are considered.
"""

import itertools

def find_combinations(candidates, target):
    def dfs(candidates, target, start, path):
        if target < 0:
            return 
        elif target == 0:
            permuts = set(itertools.permutations(path))
            for permut in permuts:
                res.append(permut)
        for i in range(start, len(candidates)):
            dfs(candidates, target-candidates[i], i, path+[candidates[i]])
    res = []
    candidates.sort()
    dfs(candidates, target, 0, [])
    return res