"""
QUESTION:
Create a function named `to_dict` that takes two lists `list1` and `list2` as input. The function should return a dictionary where elements from `list1` act as keys and elements from `list2` act as values. If `list1` and `list2` are of unequal length, the function should iterate over the shorter list. If `list1` is longer than `list2`, the remaining keys in `list1` should be assigned a default value of `None`.
"""

def to_dict(list1, list2):
    dict_res = {key: value for key, value in zip(list1, list2)}
    if len(list1) > len(list2):
        for i in range(len(list2), len(list1)):  
            dict_res[list1[i]] = None
    return dict_res