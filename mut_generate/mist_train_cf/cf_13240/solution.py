"""
QUESTION:
Write a function `find_common_elements(list1, list2)` that takes two lists as input and returns a list of common elements in sorted order. The input lists can contain duplicate elements. The function should have a time complexity less than O(n^2) and a space complexity less than O(n), where n is the length of the longest input list.
"""

def find_common_elements(list1, list2):
    common_set = set()
    for num in list1:
        if num in common_set:
            continue
        elif num in list2:
            common_set.add(num)
    for num in list2:
        if num in common_set:
            continue
        elif num in list1:
            common_set.add(num)
    return sorted(list(common_set))