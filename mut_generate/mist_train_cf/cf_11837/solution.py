"""
QUESTION:
Write a function called `extract_sort_remove_duplicates` that takes a list of strings as input. Extract the first three characters from each string, sort the resulting list in descending order, and remove any duplicate elements. The function should return the final list. The time complexity of the solution should be no more than O(n log n), where n is the total number of characters in the input list.
"""

def extract_sort_remove_duplicates(letters):
    """
    Extract the first three characters from each string in a list, 
    sort the resulting list in descending order, and remove any duplicates.

    Args:
        letters (list): A list of strings.

    Returns:
        list: A list of strings, each containing the first three characters of the input strings, 
              sorted in descending order and with duplicates removed.
    """
    return sorted(set([string[:3] for string in letters]), reverse=True)