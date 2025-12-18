"""
QUESTION:
Write a function `merge_and_sort` that takes two lists `list_a` and `list_b` as input, merges them into one list, removes any duplicate elements, and sorts the merged list in descending order without using any built-in sorting functions or libraries. The sorting should be done in-place.
"""

def merge_and_sort(list_a, list_b):
    """
    Merge two lists into one, remove any duplicate elements, and sort the merged list in descending order without using any built-in sorting functions or libraries.

    Args:
        list_a (list): The first list.
        list_b (list): The second list.

    Returns:
        list: The merged and sorted list.
    """
    # Merge the lists
    merged_list = list_a + list_b

    # Remove duplicates
    merged_list = list(set(merged_list))

    # Sort in descending order using bubble sort
    n = len(merged_list)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if merged_list[j] < merged_list[j + 1]:
                merged_list[j], merged_list[j + 1] = merged_list[j + 1], merged_list[j]

    return merged_list