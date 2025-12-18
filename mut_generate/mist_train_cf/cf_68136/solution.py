"""
QUESTION:
Implement a function called `count_items` that takes a nested dictionary `d` as input and returns two values: 
- the total count of all items in the dictionary, including both keys and values, 
- the count of keys that have dictionaries as their values.
"""

def count_items(d):
    count = 0
    dic_count = 0
    for key, val in d.items():
        count += 1
        if isinstance(val, dict):
            dic_count += 1
            inner_count, inner_dic_count = count_items(val)
            count += inner_count
            dic_count += inner_dic_count
        else:
            count += 1
    return count, dic_count