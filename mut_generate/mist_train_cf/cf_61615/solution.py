"""
QUESTION:
Implement a function `list_comparison` that takes two lists `list1` and `list2` as input, and returns a tuple of four values: 
- a list of unique elements in `list1` that are not in `list2`
- a list of unique elements in `list2` that are not in `list1`
- a list of common elements in both `list1` and `list2` without duplicates
- the difference between the sum of elements in `list1` and the sum of elements in `list2`

The function should handle lists of different lengths, repeated elements, empty lists, and negative numbers.
"""

def list_comparison(list1, list2):
    """
    This function compares two lists and returns a tuple of four values:
    - a list of unique elements in `list1` that are not in `list2`
    - a list of unique elements in `list2` that are not in `list1`
    - a list of common elements in both `list1` and `list2` without duplicates
    - the difference between the sum of elements in `list1` and the sum of elements in `list2`

    Args:
        list1 (list): The first list to compare.
        list2 (list): The second list to compare.

    Returns:
        tuple: A tuple containing four values as described above.
    """

    # Unique elements in each list
    unique_list1 = [x for x in list1 if x not in list2]
    unique_list2 = [x for x in list2 if x not in list1]

    # Common elements in both lists
    common_elements = list(set([x for x in list1 if x in list2]))

    # Difference on sum of both lists' elements
    sum_diff = sum(list1) - sum(list2)

    return unique_list1, unique_list2, common_elements, sum_diff