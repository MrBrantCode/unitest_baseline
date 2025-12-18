"""
QUESTION:
Write a function `get_unique_elements(list1, list2)` that takes two lists as input, removes duplicates within each list, combines the unique elements from both lists, and returns the resulting list while preserving the original order. The function should handle large input lists efficiently using a dictionary or set to check for duplicates.
"""

def get_unique_elements(list1, list2):
    # Create an empty set to store unique elements
    unique_elements = set()

    # Iterate over the elements of list1
    for element in list1:
        # Add each element to the set
        unique_elements.add(element)

    # Iterate over the elements of list2
    for element in list2:
        # Add each element to the set
        unique_elements.add(element)

    # Return the unique elements as a list while preserving the original order
    seen = set()
    return [x for x in list1 + list2 if not (x in seen or seen.add(x))]