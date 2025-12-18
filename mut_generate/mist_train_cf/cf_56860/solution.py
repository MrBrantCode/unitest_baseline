"""
QUESTION:
Write a function named `find_common_elements` that takes two lists as input, compares them to find the common elements (considering case sensitivity for strings), and returns a list of lists. Each sublist should contain a common element and its count, maintaining the chronological order of elements as they appear in the given lists. Do not use Python's built-in intersect functions.
"""

def find_common_elements(list1, list2):
    """
    This function compares two lists to find common elements, considering case sensitivity for strings.
    It returns a list of lists where each sublist contains a common element and its count.
    The chronological order of elements is maintained as they appear in the given lists.

    Args:
        list1 (list): The first list to compare.
        list2 (list): The second list to compare.

    Returns:
        list: A list of lists containing common elements and their counts.
    """
    output = []
    count_dict = {}

    for el in list1:
        if el in list2:
            count_dict[el] = count_dict.get(el, 0) + 1

    for key, value in count_dict.items():
        output.append([key, value])

    return output