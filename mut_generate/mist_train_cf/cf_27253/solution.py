"""
QUESTION:
Write a function `combinationSum` that takes a list of candidate numbers `candidates` and a target number `target` as input, and returns a list of all unique combinations of candidates where the candidate numbers sum to the target. Each number in `candidates` may only be used once in the combination. The solution set must not contain duplicate combinations.
"""

def combinationSum(candidates, target):
    def dfs(start, target, combination):
        if target < 0:
            return
        if target == 0:
            result.append(combination[:])
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            combination.append(candidates[i])
            dfs(i + 1, target - candidates[i], combination)
            combination.pop()

    candidates.sort()
    result = []
    dfs(0, target, [])
    return result