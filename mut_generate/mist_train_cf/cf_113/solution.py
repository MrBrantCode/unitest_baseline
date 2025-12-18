"""
QUESTION:
Write a function `find_common_elements(list1, list2)` that compares two lists and finds the common elements, considering that both lists can contain duplicate elements, and the output should only include the common elements once. The function should also find the maximum frequency of any common element. The function should have a time complexity of O(n+m), where n and m are the lengths of the two lists.

The input lists can contain up to 10^6 elements, the elements in the lists can range from 1 to 10^9, and the maximum frequency of any common element can be up to 10^6. The function should use only O(1) additional space, excluding the input and output lists.
"""

def find_common_elements(list1, list2):
    common_elements = set(list1) & set(list2)
    max_frequency = 0
    
    for element in common_elements:
        frequency = min(list1.count(element), list2.count(element))
        max_frequency = max(max_frequency, frequency)
    
    return list(common_elements), max_frequency