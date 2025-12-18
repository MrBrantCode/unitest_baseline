"""
QUESTION:
Write a function named `find_common_elements` that compares two lists and finds the common elements. The function should take two lists as input, return a list of unique common elements, and the maximum frequency of any common element. The function should have a time complexity of O(n+m), where n and m are the lengths of the two lists.
"""

def find_common_elements(list1, list2):
    common_elements = set(list1) & set(list2)
    max_frequency = 0
    frequency_dict = {}
    for element in common_elements:
        frequency_dict[element] = min(list1.count(element), list2.count(element))
        max_frequency = max(max_frequency, frequency_dict[element])
    return list(common_elements), max_frequency