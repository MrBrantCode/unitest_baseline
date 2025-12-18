"""
QUESTION:
Create a function named `shared_elements` that takes two lists as input and returns a list of unique elements common to both input lists, ordered from lowest to highest, without using built-in Python functions for sorting and eliminating duplicates. The function should return a new list containing the shared elements.
"""

def shared_elements(list1: list, list2: list) -> list:
    # Start with an empty list to store the found shared elements.
    shared = []
    # Iterate through the first input list.
    for element in list1:
        # If the element is present in the second input list and is not already stored, add it to the shared list.
        if element in list2 and element not in shared:
            shared.append(element)

    # Now sort the list using bubble sort.
    for i in range(len(shared)):
        for j in range(len(shared) - i - 1):
            if shared[j] > shared[j + 1]:
                shared[j], shared[j + 1] = shared[j + 1], shared[j]

    return shared