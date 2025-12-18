"""
QUESTION:
Create a function named `create_dictionary` that takes two lists as arguments and returns a dictionary where elements of the first list are keys and elements of the second list are values. If the lists are of unequal lengths, use elements from the longer list as keys and elements from the shorter list as values. If a key has no corresponding value, use `None` as the value. If a value appears multiple times in the second list, use the first occurrence as the corresponding value in the dictionary. Do not use built-in functions or methods such as `zip()`, `dict()`, or `enumerate()` to create the dictionary.
"""

def create_dictionary(list1, list2):
    dictionary = {}
    len1 = len(list1)
    len2 = len(list2)

    if len1 >= len2:
        longer_list = list1
        shorter_list = list2
    else:
        longer_list = list2
        shorter_list = list1

    for i in range(len(longer_list)):
        if i < len(shorter_list):
            if longer_list[i] not in dictionary:
                dictionary[longer_list[i]] = shorter_list[i]
        else:
            if longer_list[i] not in dictionary:
                dictionary[longer_list[i]] = None

    return dictionary