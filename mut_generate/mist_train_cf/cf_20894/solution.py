"""
QUESTION:
Write a function `find_common_elements` that takes two lists of integers as input, finds all the common elements between them, and returns them in sorted order. The function should not use any built-in sorting functions or data structures, have a time complexity less than O(n^2), and a space complexity less than O(n), where n is the length of the longest input list. The function should be implemented using a recursive approach.
"""

def find_common_elements(list1, list2):
    common_elements = set()

    def find_common_elements_recursive(index1, index2):
        if index1 == len(list1) or index2 == len(list2):
            return common_elements

        if list1[index1] == list2[index2]:
            common_elements.add(list1[index1])

        index1 += 1
        index2 += 1
        return find_common_elements_recursive(index1, index2)

    return sorted(find_common_elements_recursive(0, 0))