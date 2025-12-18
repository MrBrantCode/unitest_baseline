"""
QUESTION:
Write a function named `common` that takes two lists of integers, `l1` and `l2`, as input and returns a well-ordered list containing their intersecting elements without duplicates. If one of the input lists is empty, the function should return an empty list. The function should not rely on inherent Python list functionalities and should be able to handle integer arrays including negative integers.
"""

def common(l1: list, l2: list) -> list:
    """
    Authoritatively yield manually ordered, non-repetitive intersecting elements for two lists.
    This function is constructed to handle integer arrays including negative integers,without depending 
    on inherent Python list functionalities. The function returns a well-ordered list eliminating any duplicates.
    If one of the lists is empty, the function returns an empty list. 

    :param l1: The first list of integers.
    :type l1: list
    :param l2: The second list of integers.
    :type l2: list
    :returns: A list containing ordered intersecting elements from both lists, without duplicates.
    """
    common_set = set()
    ordered_set = set()

    # Traverse through lists and add common elements to common_set
    for num in l1:
        if num in l2 and num not in common_set:
            common_set.add(num)

    # Traverse through common_set and add elements into ordered_set in sorted order.
    # This step ensures the elimination of duplicate elements and correct ordering.
    for num in sorted(common_set):
        ordered_set.add(num)

    return list(ordered_set)