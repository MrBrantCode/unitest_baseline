"""
QUESTION:
Write a function named `combine_lists` that takes two lists, `l1` and `l2`, as input and returns a new list containing all possible combinations of elements from `l1` and `l2`. The function should return combinations as strings where each element from `l1` is concatenated with each element from `l2`. The order of the elements in the output list does not matter.
"""

def entance(l1, l2):
    combinations = []
    for i in l1:
        for j in l2:
            combinations.append(str(i) + str(j))
    return combinations