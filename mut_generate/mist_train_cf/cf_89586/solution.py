"""
QUESTION:
Write a function `generate_dictionary` that takes two lists, `list_a` and `list_b`, as input and returns a dictionary. The function should sort `list_a` in ascending order and `list_b` in descending order, then create a dictionary where each element in `list_a` is a key and the corresponding element in `list_b` is the value. The input lists must have the same length, and all elements in `list_a` must be unique. The elements in `list_b` must be strings.
"""

def generate_dictionary(list_a, list_b):
    list_a.sort()
    list_b.sort(reverse=True)
    return dict(zip(list_a, list_b))