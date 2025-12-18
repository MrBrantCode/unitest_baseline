"""
QUESTION:
Create a function named `create_occurrence_dict` that takes two lists, `x` and `y`, and returns a dictionary where keys are unique elements from both lists and values are the total occurrence counts of these elements in both lists. The function should handle cases where elements are present in either or both lists.
"""

def create_occurrence_dict(x, y):
    occurrence_dict = {}
    for i in set(x + y):
        occurrence_dict[i] = x.count(i) + y.count(i)
    return occurrence_dict