"""
QUESTION:
Create a function named `convert_to_list` that takes a string as input. The function should convert the input string into a list of unique elements, ignoring any leading or trailing spaces in the string and its elements. The function should also handle empty strings and case-insensitive duplicates. The time complexity of the function should be O(n), where n is the length of the input string, and the space complexity should be O(m), where m is the number of unique elements in the resulting list.
"""

def convert_to_list(string):
    string = string.strip()
    if not string:
        return []
    string = string.lower()
    elements = string.split(",")
    elements = [element.strip() for element in elements]
    unique_elements = set()
    for element in elements:
        if element not in unique_elements:
            unique_elements.add(element)
    unique_elements_list = list(unique_elements)
    unique_elements_list = [element.upper() for element in unique_elements_list]
    return unique_elements_list