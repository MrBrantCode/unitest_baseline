"""
QUESTION:
Write a function `combinationSum2(candidates, target)` that takes a list of integers `candidates` and a target integer `target` as input. Return all distinct combinations within `candidates` that sum up to `target`, where each digit in `candidates` can only be utilized once in a single combination. The solution set should not include any repeated combinations. The length of `candidates` is between 1 and 100, and each element in `candidates` is between 1 and 50. The `target` is between 1 and 30.
"""

def combinationSum2(candidates, target):
    def dfs(candidates, target, start, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return 
        for i in range(start, len(candidates)):
            # i > start ensures that no duplication of sets in the combination 
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            # explore remaining part
            dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]], res)

    candidates.sort()
    res = []
    dfs(candidates, target, 0, [], res)
    return res