"""
QUESTION:
Write a function named `insert_elements` that inserts n new elements at the beginning of a given list, where n is the length of the list. The new elements should be strings in the format "x1", "x2", ..., "xn". The solution should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the list.
"""

def insert_elements(lst):
    n = len(lst)
    for i in range(n):
        lst.insert(i, "x" + str(n-i))
    return lst