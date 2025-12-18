"""
QUESTION:
Write a function named "subset_check" that determines if one set is a subset of another set without using any set methods in the Python standard library. The function should take two sets as input and return 'True' if the first set is a subset of the second or 'False' otherwise. The function should be efficient, particularly when dealing with large sets.
"""

def subset_check(s1, s2):
    s2_dict = {i : 1 for i in s2}
    for i in s1:
        if i not in s2_dict:
            return False
    return True