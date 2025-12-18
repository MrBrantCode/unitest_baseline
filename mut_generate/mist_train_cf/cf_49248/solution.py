"""
QUESTION:
Create a function named `common_elements` that takes two lists `list1` and `list2` as input and returns a list of elements that appear in both lists an equal number of times. The function should ignore elements that do not have the same frequency in both lists.
"""

from collections import Counter

def common_elements(list1, list2):
    common = []
    counter_list1 = Counter(list1)
    counter_list2 = Counter(list2)
    for k, v in counter_list1.items():
        if k in counter_list2 and v == counter_list2[k]:
            common.extend([k]*v)
    return common