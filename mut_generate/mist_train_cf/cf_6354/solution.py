"""
QUESTION:
Create a function named `find_common_elements` that takes two lists `list1` and `list2` as parameters. The function should remove duplicates from both input lists, sort the lists in ascending order, find the common elements, and return the sorted list of common elements. The function should not use any built-in functions or libraries except for `len()`, `range()`, and `int()`. The time complexity of the function should be O(n).
"""

def find_common_elements(list1, list2):
    def remove_duplicates(lst):
        result = []
        for element in lst:
            if element not in result:
                result.append(element)
        return result

    def sort_list(lst):
        for i in range(len(lst)):
            min_index = i
            for j in range(i + 1, len(lst)):
                if lst[j] < lst[min_index]:
                    min_index = j
            lst[i], lst[min_index] = lst[min_index], lst[i]
        return lst

    list1 = remove_duplicates(list1)
    list2 = remove_duplicates(list2)

    list1 = sort_list(list1)
    list2 = sort_list(list2)

    common_elements = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            common_elements.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1

    return common_elements