"""
QUESTION:
Insert n new elements at the beginning of a list, where n is the length of the list. The function should be named `insert_elements` and it should take a list as input. The new elements should be strings in the format "x1", "x2", etc. The time complexity of the solution should be O(n), where n is the length of the list, and the space complexity should be O(n).
"""

def insert_elements(lst):
    n = len(lst)
    for i in range(n):
        lst.insert(0, "x" + str(n-i))
    return lst