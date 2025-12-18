"""
QUESTION:
Write a function `find_common_elements(list1, list2, list3)` that finds the common elements among three input lists without using set or in-built functions. The function should optimize the comparison process by starting with the shortest list to minimize the number of comparisons.
"""

def find_common_elements(list1, list2, list3):
    """
    Finds the common elements among three input lists without using set or in-built functions.

    Args:
        list1 (list): The first list.
        list2 (list): The second list.
        list3 (list): The third list.

    Returns:
        list: A list of common elements among the three input lists.
    """

    # Determine the shortest list to minimize the comparisons
    shortest_list = list1
    if len(list2) < len(shortest_list):
        shortest_list = list2
    if len(list3) < len(shortest_list):
        shortest_list = list3

    # Find the common elements
    common_elements = []
    for i in shortest_list:
        if i in list1 and i in list2 and i in list3:
            common_elements.append(i)
    return common_elements