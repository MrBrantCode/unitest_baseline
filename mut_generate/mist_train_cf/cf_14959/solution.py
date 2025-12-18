"""
QUESTION:
Create a function `find_unique_elements` that takes a list of integers as input and returns a new list containing only the unique elements in the order of their first appearance. The function must achieve this with a time complexity of O(n) and a space complexity of O(n), where n represents the length of the input list.
"""

def find_unique_elements(lst):
    unique_elements = []
    seen = set()
    for num in lst:
        if num not in seen:
            unique_elements.append(num)
            seen.add(num)
    return unique_elements