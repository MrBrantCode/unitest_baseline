"""
QUESTION:
Write a function `combinationSum` that takes a list of integers `candidates` and an integer `target` as input and returns all unique combinations of integers in the `candidates` list that sum up to the `target`. Each number in `candidates` may only be used once in the combination, and the solution set must not contain duplicate combinations.
"""

def combinationSum(candidates, target):
    def backtrack(start, path, target):
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            backtrack(i + 1, path + [candidates[i]], target - candidates[i])

    candidates.sort()
    result = []
    backtrack(0, [], target)
    return result