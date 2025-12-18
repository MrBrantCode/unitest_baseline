"""
QUESTION:
Write a function `find_duplicates` that takes a list of elements as input and returns a list of duplicate elements found in the input list. The output list should contain each duplicate element only once.
"""

def find_duplicates(lst):
    duplicate_elements = []
    for element in lst:
        if lst.count(element) > 1 and element not in duplicate_elements:
            duplicate_elements.append(element)
    return duplicate_elements