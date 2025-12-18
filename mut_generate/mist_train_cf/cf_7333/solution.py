"""
QUESTION:
Write a function `compare_lists(list1, list2)` to compare two lists, considering the order and type of elements, including nested lists, dictionaries, tuples, and sets. The function should have a time complexity of O(n), where n is the length of the longer list, and a space complexity of O(1). If the lists are equal, the function should print "The lists are equal" and return True; otherwise, it should print "The lists are not equal" and return.
"""

def entance(list1, list2):
    if len(list1) != len(list2):
        print("The lists are not equal")
        return False

    for i in range(len(list1)):
        if type(list1[i]) != type(list2[i]):
            print("The lists are not equal")
            return False

        if isinstance(list1[i], list):
            if not entance(list1[i], list2[i]):
                print("The lists are not equal")
                return False

        elif isinstance(list1[i], dict):
            if list1[i] != list2[i]:
                print("The lists are not equal")
                return False

        elif isinstance(list1[i], tuple):
            if list1[i] != list2[i]:
                print("The lists are not equal")
                return False

        elif isinstance(list1[i], set):
            if list1[i] != list2[i]:
                print("The lists are not equal")
                return False

        elif list1[i] != list2[i]:
            print("The lists are not equal")
            return False

    print("The lists are equal")
    return True