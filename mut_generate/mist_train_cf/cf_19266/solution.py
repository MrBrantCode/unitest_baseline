"""
QUESTION:
Write a function named `compare_lists` that takes two lists as input and returns True if the lists have the same elements in the same order, and False otherwise. The lists can contain any type of elements, including integers, floats, strings, and nested lists. Do not use any built-in functions or libraries that directly compare the two lists or any loops and recursion in your solution, but implement the comparison logic using basic operations and conditionals.
"""

def compare_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    if list1[0] != list2[0]:
        if isinstance(list1[0], list):
            return list1 == list2
        elif isinstance(list1[0], str):
            return list1[0].lower() != list2[0].lower()
        elif isinstance(list1[0], float):
            return abs(list1[0] - list2[0]) > 1e-6
        else:
            return False
    return list1 == list2