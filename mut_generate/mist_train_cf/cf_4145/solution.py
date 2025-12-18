"""
QUESTION:
Write a Python function `get_unique_elements(list1, list2)` that takes two lists as input, removes duplicates within each list, and returns a new list containing the unique elements from both lists in their original order. The function should handle input lists with up to 10^6 elements efficiently using a dictionary or set to check for duplicates and store unique elements.
"""

def entrance(list1, list2):
    unique_elements = []
    seen_elements = set()

    for element in list1 + list2:
        if element not in seen_elements:
            unique_elements.append(element)
            seen_elements.add(element)

    return unique_elements