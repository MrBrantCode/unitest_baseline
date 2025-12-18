"""
QUESTION:
Create a function named 'mergeAndSortTwoLists' that takes two lists and a boolean as arguments. The function should merge the two lists into one, remove any duplicates, and sort the resulting list in either ascending or descending order based on the boolean value (True for ascending, False for descending). The function should be able to handle lists containing both integers and floats, and should be efficient enough to handle large lists of up to 1,000,000 elements.
"""

def mergeAndSortTwoLists(list1, list2, ascending=True):
    merged = list(set(list1 + list2))
    merged.sort(reverse=not ascending)
    return merged