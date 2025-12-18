"""
QUESTION:
Write a function `find_max_depth` that finds the maximum depth of a given nested list, which can contain both integers and strings, as well as other nested lists. The function should return a tuple containing the maximum depth and the corresponding index of the deepest element. The function must have a time complexity of O(n), where n is the total number of elements in the nested list.
"""

def find_max_depth(nested_list):
    """
    Finds the maximum depth of a given nested list and returns it along with the index of the deepest element.

    Args:
        nested_list (list): A list that can contain both integers and strings, as well as other nested lists.

    Returns:
        tuple: A tuple containing the maximum depth and the corresponding index of the deepest element.
    """

    max_depth = 0
    deepest_index = ()
    
    def dfs(nested_list, depth, index):
        """
        Performs a depth-first search (DFS) traversal on the nested list.

        Args:
            nested_list (list): The current nested list being traversed.
            depth (int): The current depth of the traversal.
            index (tuple): The current index of the traversal.
        """
        nonlocal max_depth, deepest_index
        
        if depth > max_depth:
            max_depth = depth
            deepest_index = index
        
        for i, elem in enumerate(nested_list):
            if isinstance(elem, list):
                dfs(elem, depth + 1, index + (i,))
    
    dfs(nested_list, 1, ())
    return max_depth, deepest_index