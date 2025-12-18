"""
QUESTION:
Develop a function `most_seldom_element` that identifies the most seldom appearing element within a provided list. The function should return the element with its frequency of occurrence. If there are multiple least common elements, it should return one of them. Assume the input list contains hashable elements. The function should raise an exception if the input list is empty.
"""

import collections

def most_seldom_element(lst):
    if not lst:
        raise Exception("Input list is empty")
    
    counter = collections.Counter(lst)
    return counter.most_common()[-1]