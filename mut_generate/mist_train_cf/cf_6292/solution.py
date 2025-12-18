"""
QUESTION:
Write a function called `find_common_elements` that finds all the common elements between two lists of integers and returns them in sorted order. The function should have a time complexity of less than O(n^2) and a space complexity of less than O(n), where n is the length of the longest input list. The function should be implemented using a recursive approach and should not use any built-in sorting functions or data structures. The input lists can contain duplicate elements, but the common elements should not include any duplicates.
"""

def find_common_elements(list1, list2):
    common_elements = []

    def find_common_helper(i, j):
        if i >= len(list1) or j >= len(list2):
            return

        if list1[i] == list2[j]:
            if len(common_elements) == 0 or list1[i] != common_elements[-1]:
                common_elements.append(list1[i])

            find_common_helper(i + 1, j + 1)
        elif list1[i] < list2[j]:
            find_common_helper(i + 1, j)
        else:
            find_common_helper(i, j + 1)

    find_common_helper(0, 0)

    return sorted(common_elements)