"""
QUESTION:
Write a function `find_index_recursive` that finds all instances of a target integer in a multidimensional array and returns their indices. The function should return an empty list if the target is not found. The indices should be returned as a multidimensional list, where the inner lists represent nested positions within the original array. The function should handle arrays of arbitrary depth.
"""

def find_index_recursive(arr, target):
    indices = []
    def recursive_search(arr, target, current_path):
        for i, value in enumerate(arr):
            if isinstance(value, list):
                recursive_search(value, target, current_path + [i])
            elif value == target:
                indices.append(current_path + [i])
                
    recursive_search(arr, target, [])
    return indices