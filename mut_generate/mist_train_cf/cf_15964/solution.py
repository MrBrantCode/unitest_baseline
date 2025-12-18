"""
QUESTION:
Create a function named combine_lists that takes two lists of equal length as input, list1 and list2. The function should return a dictionary where the keys are elements from list1 and the values are lists of corresponding elements from list2 that are divisible by 2. If there are multiple occurrences of the same key in list1, the corresponding values in list2 should be combined into a single list. The resulting dictionary should be sorted in descending order based on the keys.
"""

def combine_lists(list1, list2):
    result_dict = {}
    for i in range(len(list1)):
        if list2[i] % 2 == 0:
            if list1[i] in result_dict:
                result_dict[list1[i]].append(list2[i])
            else:
                result_dict[list1[i]] = [list2[i]]
    return dict(sorted(result_dict.items(), key=lambda x: x[0], reverse=True))