"""
QUESTION:
Compare two lists with the function `compare_lists(list1, list2)` considering order of elements and handling nested lists, dictionaries, tuples, and sets. The function should have a time complexity of O(n), where n is the length of the longer list, and a space complexity of O(1).
"""

def compare_lists(list1, list2):
    if len(list1) != len(list2):
        return False

    for i in range(len(list1)):
        if type(list1[i]) != type(list2[i]):
            return False

        if isinstance(list1[i], list):
            if not compare_lists(list1[i], list2[i]):
                return False

        elif isinstance(list1[i], dict):
            if list1[i] != list2[i]:
                return False

        elif isinstance(list1[i], tuple):
            if list1[i] != list2[i]:
                return False

        elif isinstance(list1[i], set):
            if list1[i] != list2[i]:
                return False

        elif list1[i] != list2[i]:
            return False

    return True