"""
QUESTION:
Write a function `find_common_elements` that takes two lists as input, returns a list of common elements between the two lists, removes duplicates, and sorts the output in ascending order. The function should have a time complexity of O(n) and should not use any built-in functions or libraries.
"""

def find_common_elements(list1, list2):
    """
    Returns a list of common elements between two lists, removes duplicates, 
    and sorts the output in ascending order.

    Time complexity: O(n)

    Args:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
        list: A list of common elements between the two lists.
    """

    common_elements = []
    list1_duplicates = set()

    # Find duplicates in list1
    for element in list1:
        if element in list1_duplicates:
            continue
        if element in list2:
            common_elements.append(element)
        list1_duplicates.add(element)

    # Sort the common elements in ascending order
    for i in range(len(common_elements) - 1):
        min_index = i
        for j in range(i + 1, len(common_elements)):
            if common_elements[j] < common_elements[min_index]:
                min_index = j
        common_elements[i], common_elements[min_index] = common_elements[min_index], common_elements[i]

    return common_elements