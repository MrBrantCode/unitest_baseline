"""
QUESTION:
Write a function named `compare_lists` that compares two given lists and returns `True` if their contents are the same and in the same order. The function should return `False` if the lists contain duplicate elements or if their contents are not the same. The function should have a time complexity of O(n), where n is the length of the lists, and should use only constant space.
"""

def compare_lists(list1, list2):
    if len(list1) != len(list2):
        return False

    frequency = {}

    for element in list1:
        if element in frequency:
            return False
        else:
            frequency[element] = 1

    for element in list2:
        if element not in frequency:
            return False
        else:
            frequency[element] -= 1
            if frequency[element] == 0:
                del frequency[element]

    return not bool(frequency)