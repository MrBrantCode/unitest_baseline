"""
QUESTION:
Create a function `intersecting_elements(list1, list2)` that finds the intersecting elements of two input lists and returns them in descending order of their combined frequencies. The function should be able to handle lists with up to 1000 elements and cases where the input lists contain duplicate elements.
"""

from collections import Counter

def intersecting_elements(list1, list2):
    """
    This function finds the intersecting elements of two input lists 
    and returns them in descending order of their combined frequencies.

    Parameters:
    list1 (list): The first input list.
    list2 (list): The second input list.

    Returns:
    list: A list of tuples, where each tuple contains an intersecting element 
          and its frequency in the combined list.
    """
    intersect = list(set(list1) & set(list2))
    freq = Counter(list1 + list2)
    result = [(elem, freq[elem]) for elem in intersect]
    result.sort(key=lambda x: x[1], reverse=True)
    return result