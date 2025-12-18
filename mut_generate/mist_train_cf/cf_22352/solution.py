"""
QUESTION:
Create a function named `find_common_elements` that takes two lists as input, `list1` and `list2`, and returns a list containing all the common elements, without any duplicates, in ascending order. The function should have a time complexity of O(n log n), where n is the total number of elements in both lists. The function should be able to handle lists with up to 10,000 elements.
"""

def find_common_elements(list1, list2):
    list1.sort()
    list2.sort()

    pointer1 = 0
    pointer2 = 0

    common_elements = []

    while pointer1 < len(list1) and pointer2 < len(list2):
        if list1[pointer1] == list2[pointer2]:
            if not common_elements or common_elements[-1] != list1[pointer1]:
                common_elements.append(list1[pointer1])
            pointer1 += 1
            pointer2 += 1
        elif list1[pointer1] < list2[pointer2]:
            pointer1 += 1
        else:
            pointer2 += 1

    return common_elements