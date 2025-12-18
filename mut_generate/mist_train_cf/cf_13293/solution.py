"""
QUESTION:
Write a function `common_elements` that takes two lists as input and returns a list of common elements between them, with duplicates removed and sorted in ascending order. The function should have a time complexity of O(n) and should not use any built-in functions or libraries.
"""

def common_elements(list1, list2):
    common_elements = []
    list1_duplicates = set()

    for element in list1:
        if element in list1_duplicates:
            continue
        if element in list2:
            common_elements.append(element)
        list1_duplicates.add(element)

    for i in range(len(common_elements) - 1):
        min_index = i
        for j in range(i + 1, len(common_elements)):
            if common_elements[j] < common_elements[min_index]:
                min_index = j
        common_elements[i], common_elements[min_index] = common_elements[min_index], common_elements[i]

    return common_elements