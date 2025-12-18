"""
QUESTION:
Write a function `common_elements(groupA, groupB, groupC, groupD, exclude=None)` that finds the common elements among four sets `groupA`, `groupB`, `groupC`, and `groupD`. The function should also allow excluding a specific set from the intersection operation by passing the name of the set to be excluded as a string in the `exclude` parameter.
"""

def common_elements(groupA, groupB, groupC, groupD, exclude=None):
    """
    Finds the common elements among four sets groupA, groupB, groupC, and groupD.
    Allows excluding a specific set from the intersection operation by passing 
    the name of the set to be excluded as a string in the exclude parameter.

    Args:
    groupA (set): The first set.
    groupB (set): The second set.
    groupC (set): The third set.
    groupD (set): The fourth set.
    exclude (str, optional): The name of the set to be excluded. Defaults to None.

    Returns:
    set: A set of common elements among the input sets.
    """

    if exclude:
        if exclude == 'groupA':
            return groupB & groupC & groupD
        elif exclude == 'groupB':
            return groupA & groupC & groupD
        elif exclude == 'groupC':
            return groupA & groupB & groupD
        elif exclude == 'groupD':
            return groupA & groupB & groupC
    else:
        return groupA & groupB & groupC & groupD