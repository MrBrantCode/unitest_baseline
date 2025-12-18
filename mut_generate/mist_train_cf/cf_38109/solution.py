"""
QUESTION:
Write a function `combinationSum` that takes a list of integers `candidates` and a target integer `target` as input and returns a list of all unique combinations of numbers in `candidates` that sum up to `target`. Each number in `candidates` may be used an unlimited number of times, and the numbers within a combination should be in non-descending order.
"""

from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    def backtracking(start_index, remain, sub_solution, solution):
        if remain == 0:
            solution.append(sub_solution[:])  # Append a copy of sub_solution to the solution list
            return
        for i in range(start_index, len(candidates)):
            if remain - candidates[i] >= 0:
                backtracking(i, remain - candidates[i], sub_solution + [candidates[i]], solution)

    candidates.sort()  # Sort the candidates list to ensure non-descending order
    solution = []
    backtracking(0, target, [], solution)
    return solution