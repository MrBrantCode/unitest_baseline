"""
QUESTION:
Write a function named `count_unique_strings` that takes a list of elements as input, where each element is either an integer or a string, and returns the count of unique strings in the list. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the number of elements in the list.
"""

def count_unique_strings(list_elements):
    unique_strings = set()
    
    for element in list_elements:
        if isinstance(element, str) and element not in unique_strings:
            unique_strings.add(element)
    
    return len(unique_strings)