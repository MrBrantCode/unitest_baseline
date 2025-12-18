"""
QUESTION:
Write a function `combinationSum(candidates, target)` that returns all unique combinations of candidates where the chosen numbers sum to the target. Each number in candidates may be used an unlimited number of times. The function takes two parameters: `candidates`, a list of distinct integers, and `target`, a target integer.
"""

def combinationSum(candidates, target):
    def backtrack(start, target, path):
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(candidates)):
            backtrack(i, target - candidates[i], path + [candidates[i]])

    result = []
    backtrack(0, target, [])
    return result