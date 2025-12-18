"""
QUESTION:
Write a function named `get_unique_elements` that takes a list of integers as input and returns a new list containing only the unique elements from the input list. The function must have a time complexity of O(n) and a space complexity of O(n), where n is the number of elements in the input list. The implementation should not use any built-in functions or libraries for counting or checking for uniqueness.
"""

def get_unique_elements(lst):
    unique_elements = []
    seen = set()
    for element in lst:
        if element not in seen:
            seen.add(element)
            unique_elements.append(element)
    return unique_elements