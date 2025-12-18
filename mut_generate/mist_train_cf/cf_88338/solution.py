"""
QUESTION:
Write a Python function named `get_unique_elements` that takes two lists, `list1` and `list2`, as input and returns a new list containing unique elements from both lists. The function should remove duplicates within each list, preserve the original order of elements, and handle up to 10^6 elements efficiently without performance issues by using a dictionary or set for duplicate checking.
"""

def get_unique_elements(list1, list2):
    unique_elements = []
    seen_elements = set()

    for element in list1 + list2:
        if element not in seen_elements:
            unique_elements.append(element)
            seen_elements.add(element)

    return unique_elements