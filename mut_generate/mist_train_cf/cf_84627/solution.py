"""
QUESTION:
Create a function called `combine` that takes two lists as input, `list1` and `list2`, and returns a list containing every possible combination of one element from `list1` and one element from `list2`. The function should not use any built-in itertools functions and should not include any duplicate combinations in the resulting list.
"""

def combine(list1, list2):
    """
    This function takes two lists as input, list1 and list2, 
    and returns a list containing every possible combination 
    of one element from list1 and one element from list2.

    Args:
        list1 (list): The first list of elements.
        list2 (list): The second list of elements.

    Returns:
        list: A list of lists, where each sublist is a combination 
        of one element from list1 and one element from list2.
    """
    combinations = []
    for i in list1:
        for j in list2:
            pair = [i, j]
            if pair not in combinations:
                combinations.append(pair)
    return combinations