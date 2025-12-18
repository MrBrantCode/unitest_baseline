"""
QUESTION:
Write a function `find_common_elements(list1, list2)` that compares two lists and returns the common elements, considering that both lists can contain duplicate elements. The function should have a time complexity of O(n+m), where n and m are the lengths of the two lists, and the output should include each common element only once.
"""

from collections import Counter

def find_common_elements(list1, list2):
    # Count the occurrences of each element in both lists
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    
    # Find the common elements
    common_elements = []
    for element in counter1:
        if element in counter2:
            common_elements.append(element)
    
    return common_elements