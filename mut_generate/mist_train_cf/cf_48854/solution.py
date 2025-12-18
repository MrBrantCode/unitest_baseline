"""
QUESTION:
Write a function `permute_two_lists(list1, list2)` that generates all possible permutations of pairs from two input lists `list1` and `list2`, preserving the positional consistency of elements from both lists. The function should return or print all pairs of permutations where each element from `list1` is paired with every element from `list2`.
"""

def permute_two_lists(list1, list2):
    """
    This function generates all possible permutations of pairs from two input lists, 
    preserving the positional consistency of elements from both lists.

    Args:
        list1 (list): The first input list.
        list2 (list): The second input list.

    Returns:
        list: A list of all pairs of permutations where each element from list1 is paired with every element from list2.
    """
    permutation_list = []
    for i in list1:
        for j in list2:
            permutation_list.append([i, j])
    return permutation_list