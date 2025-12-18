"""
QUESTION:
Create a function named `compare_lists` that compares two distinct lists, `list1` and `list2`, to identify common elements and their respective indices in each list without using any built-in Python methods for comparison or list manipulation. The function should return the shared components and their indices in both lists as a dictionary.
"""

def compare_lists(list1, list2):
    """
    Compare two distinct lists to identify common elements and their respective indices.

    Args:
    list1 (list): The first list.
    list2 (list): The second list.

    Returns:
    dict: A dictionary containing common elements as keys and their indices in both lists as values.
    """
    common_elements = {}
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                if list1[i] not in common_elements:
                    common_elements[list1[i]] = [(i,j)]
                else:
                    common_elements[list1[i]].append((i,j))
    return common_elements