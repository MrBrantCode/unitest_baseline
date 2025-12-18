"""
QUESTION:
Write a function `extract_elements` that takes a list as input and returns a new list containing the first 3 elements of the input list. The function should not use Python's built-in slicing functionality. If the input list has fewer than 3 elements, the function should return all elements in the list.
"""

def extract_elements(lst):
    extracted_elements = []
    for i in range(min(3, len(lst))):
        extracted_elements.append(lst[i])
    return extracted_elements