"""
QUESTION:
Create a function named `unique_same_elements` that takes a list of lists as input and returns the count of unique sublists containing identical elements. The function should handle lists of any data types, including empty lists, and should have a time complexity of O(n). The function should return 0 if no such sublists exist.
"""

def unique_same_elements(lists):
    unique_lists = {}
    for lst in lists:
        if len(set(lst)) == 1 and len(lst) != 0:
            frozen = frozenset(lst)
            if frozen in unique_lists:
                unique_lists[frozen] += 1
            else:
                unique_lists[frozen] = 1
    return sum(unique_lists.values())