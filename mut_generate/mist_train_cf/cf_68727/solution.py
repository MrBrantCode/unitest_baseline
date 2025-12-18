"""
QUESTION:
Construct a function `keep_least_common` that takes a list of elements (which can be a mix of float and Boolean values) and returns the five least common unique elements in the list. If there are less than five unique elements, return all of them. The function should be able to handle multiple elements tied for least common and can return them in any order.
"""

from collections import Counter

def keep_least_common(lst):
    counter = Counter(lst)
    counter_least_common = counter.most_common()[:-6:-1]
    least_common_elements = [item[0] for item in counter_least_common]
    return least_common_elements