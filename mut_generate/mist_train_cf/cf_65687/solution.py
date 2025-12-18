"""
QUESTION:
Write a function called `find_combinations` that takes an integer `target_weight` and a list of integers `pear_weights` as input. The function should return all possible combinations of pears that sum up to the target weight, assuming that only integer values are allowed and that the same type of pear can be used multiple times.
"""

def find_combinations(target_weight, pear_weights):
    def dfs(target, start, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return 
        for i in range(start, len(pear_weights)):
            dfs(target-pear_weights[i], i, path+[pear_weights[i]], res)
            
    res = []
    dfs(target_weight, 0, [], res)
    return res