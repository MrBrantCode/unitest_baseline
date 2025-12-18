"""
QUESTION:
Write a function `compare_lists(list1, list2)` that compares two given lists and returns `True` if their contents are the same, including the order of elements, and `False` otherwise. The function should not use any additional data structures or variables whose size scales with the input size and should handle cases where the lists contain duplicate elements. If any of the lists contain duplicate elements, the function should return `False`. The time complexity should be O(n), where n is the length of the lists.
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