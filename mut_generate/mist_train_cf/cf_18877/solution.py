"""
QUESTION:
Write a function called `find_max_depth` that takes a nested list as input and returns a tuple containing the maximum depth of the list and the corresponding index of the deepest element. The function should have a time complexity of O(n), where n is the total number of elements in the nested list. The nested list can contain both integers and strings, as well as other nested lists.
"""

def find_max_depth(nested_list):
    max_depth = 0
    deepest_index = ()
    
    def dfs(nested_list, depth, index):
        nonlocal max_depth, deepest_index
        
        if depth > max_depth:
            max_depth = depth
            deepest_index = index
        
        for i, elem in enumerate(nested_list):
            if isinstance(elem, list):
                dfs(elem, depth + 1, index + (i,))
    
    dfs(nested_list, 1, ())
    return max_depth, deepest_index