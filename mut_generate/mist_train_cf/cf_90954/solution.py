"""
QUESTION:
Create a function `combine_lists` that takes two lists of equal length, `list1` and `list2`, as input. The function should return a dictionary where each key-value pair consists of an element from `list1` and its corresponding elements from `list2` that are divisible by 2. If there are multiple corresponding elements in `list2` for the same element in `list1`, they should be stored as a list of values in the dictionary.
"""

def combine_lists(list1, list2):
    result_dict = {}
    for i in range(len(list1)):
        if list2[i] % 2 == 0:
            if list1[i] in result_dict:
                result_dict[list1[i]].append(list2[i])
            else:
                result_dict[list1[i]] = [list2[i]]
    return result_dict