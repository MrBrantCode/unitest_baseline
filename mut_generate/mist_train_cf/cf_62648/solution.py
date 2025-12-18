"""
QUESTION:
Write a function named `find_combinations` that generates all possible combinations of subarrays from the input array `candidates` whose sum is equal to the given `target`. The function should return a list of these combinations. Note that the same number can be used repeatedly in a combination.
"""

def find_combinations(candidates, target):
    result = []
    def _find_combinations(start_index, candidates, target, current_combination):
        if target == 0:
            result.append(list(current_combination))
            return
        
        for i in range(start_index, len(candidates)):
            if candidates[i] > target:
                break
            
            current_combination.append(candidates[i])
            _find_combinations(i, candidates, target - candidates[i], current_combination)
            current_combination.pop()

    _find_combinations(0, candidates, target, [])
    return result