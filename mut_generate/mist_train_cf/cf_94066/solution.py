"""
QUESTION:
Write a function `convert_to_list` that takes a comma-separated string as input. The function should return a list of unique elements from the string, ignoring any leading or trailing spaces, and considering duplicates case-insensitively. The function should have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(m), where m is the number of unique elements in the resulting list. If the input string is empty, the function should return an empty list.
"""

def convert_to_list(input_string):
    input_string = input_string.strip()
    
    if not input_string:
        return []
    
    elements = input_string.split(',')
    unique_elements = set([element.strip().lower() for element in elements])
    
    return list(unique_elements)