"""
QUESTION:
Create a function named "sort_and_remove_duplicates" that sorts a given list of integers in descending order using selection sort and removes any duplicate values. The function should not take any parameters and should return the sorted list. The input list should be iterated through, and any duplicate values should be skipped.
"""

def sort_and_remove_duplicates(input_list):
    """
    Sorts a given list of integers in descending order using selection sort and removes any duplicate values.

    Args:
    input_list (list): A list of integers to be sorted and have duplicates removed.

    Returns:
    list: A sorted list of unique integers in descending order.
    """

    sorted_list = []
    given_list = input_list.copy()  # Create a copy of the input list

    while given_list:
        maximum = max(given_list)
        if maximum in sorted_list:
            given_list.remove(maximum)
            continue

        sorted_list.append(maximum)
        given_list.remove(maximum)

    return sorted_list