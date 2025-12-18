"""
QUESTION:
Implement a function `find_max_and_path(lst)` that finds the maximum element in a multilayered, non-uniform hierarchical array and returns its value along with its location hierarchy in the structure. The function should work with arrays that may contain `None` values and nested lists of varying depths.
"""

def find_max_and_path(lst):
    max_val = float('-inf')
    max_path = []

    def dfs(lst, path):
        nonlocal max_val, max_path
        for i, val in enumerate(lst):
            new_path = path + [i]
            if isinstance(val, list):
                dfs(val, new_path)
            else:
                if val is not None and val > max_val:
                    max_val = val
                    max_path = new_path

    dfs(lst, [])
    return max_val, max_path