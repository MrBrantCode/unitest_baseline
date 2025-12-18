"""
QUESTION:
Create a function `find_common_elements` that takes two lists as input, finds their common elements while ignoring duplicates, and returns a list of unique common elements. The function should have a time complexity of O(n+m), where n and m are the lengths of the two input lists.
"""

from collections import Counter

def find_common_elements(list1, list2):
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    
    common_elements = []
    for element in counter1:
        if element in counter2:
            common_elements.append(element)
    
    return common_elements