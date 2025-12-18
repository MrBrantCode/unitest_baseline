"""
QUESTION:
Write a function called `combine_lists` that takes two lists of strings of equal length as input. The function should return a dictionary where keys are from the first list and values are from the second list. If there are duplicate keys, the function should append the corresponding values to the existing keys instead of overwriting them.
"""

def combine_lists(list1, list2):
    result = {}
    for i in range(len(list1)):
        if list1[i] in result:
            result[list1[i]].append(list2[i])
        else:
            result[list1[i]] = [list2[i]]
    return result