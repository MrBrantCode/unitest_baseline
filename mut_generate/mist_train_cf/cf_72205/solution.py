"""
QUESTION:
Develop a function named `common_elements` that identifies common elements in two given sets, determines the set from which the common element originated, and returns a dictionary where the keys are the common elements and the values are tuples. The tuple values should contain two elements: the count of the common element and a string indicating the originating set ("set1", "set2", or "both" if present in both). However, since sets in Python cannot contain duplicates, the counts will always be 1 for each set.
"""

def common_elements(set1, set2):
    common_dict = {}
    for element in set1.intersection(set2):
        common_dict[element] = (1, 'both')
    return common_dict