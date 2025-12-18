"""
QUESTION:
Write a function `convert_to_list` that takes a comma-separated string as input, removes any leading or trailing spaces from the string and its elements, checks for empty strings, and returns a list of unique elements in a case-insensitive manner. The function should have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(m), where m is the number of unique elements in the resulting list.
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