"""
QUESTION:
Write a function called `permute` that takes a list of distinct alphanumeric characters as input and returns a list of all unique permutations of the input list. The function should be implemented recursively. The input list may be empty or contain any number of distinct alphanumeric characters.
"""

def permute(lst):
    """
    Returns a list of all unique permutations of the input list.
    
    Args:
        lst (list): A list of distinct alphanumeric characters.
    
    Returns:
        list: A list of all unique permutations of the input list.
    """
    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]

    result = []

    for i in range(len(lst)):
        current_element = lst[i]
        remaining_list = lst[:i] + lst[i+1:]

        for permutation in permute(remaining_list):
            result.append([current_element] + permutation)

    return result