"""
QUESTION:
Write a function `findCommonElements` that takes two arrays `array1` and `array2` as input and returns the common elements between them. The function should achieve this in O(n) time complexity, where n is the size of the larger array, and without using any additional data structures, built-in functions, or explicit loops (such as for, while, or do-while). Use recursion instead.
"""

def findCommonElements(array1, array2):
    def recursive_common_elements(index1, index2, element_map, common_elements):
        if index1 == len(array1):
            if index2 == len(array2):
                return common_elements
            else:
                return recursive_common_elements(index1, index2 + 1, element_map, common_elements)
        else:
            if array1[index1] not in element_map:
                element_map[array1[index1]] = 1
            else:
                element_map[array1[index1]] += 1
            return recursive_common_elements(index1 + 1, index2, element_map, common_elements)

    def recursive_find_common(index, element_map, common_elements):
        if index == len(array2):
            return common_elements
        else:
            if array2[index] in element_map and element_map[array2[index]] > 0:
                common_elements.append(array2[index])
                element_map[array2[index]] -= 1
            return recursive_find_common(index + 1, element_map, common_elements)

    element_map = {}
    common_elements = []
    recursive_common_elements(0, 0, element_map, common_elements)
    return recursive_find_common(0, element_map, common_elements)