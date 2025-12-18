"""
QUESTION:
Create a function `intersecting_elements(list1, list2)` that finds the intersecting elements of two lists and returns them in descending order of their frequency. The function should be able to handle input lists with up to 1000 elements and cases where the input lists contain duplicate elements. The function should return a list of tuples where each tuple contains an intersecting element and its total frequency in both lists.
"""

from collections import Counter

def intersecting_elements(list1, list2):
    intersect = list(set(list1) & set(list2))
    freq = Counter(list1 + list2)
    result = [(elem, freq[elem]) for elem in intersect]
    return sorted(result, key=lambda x: x[1], reverse=True)