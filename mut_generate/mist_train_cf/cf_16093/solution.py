"""
QUESTION:
Write a function `convert_to_list` that takes a comma-separated string as input, converts it into a list, and returns the list. The function should ignore any leading or trailing spaces in the input string and handle empty strings by returning an empty list. It should also remove any duplicate elements from the list in a case-insensitive manner, where "A" and "a" are considered the same element. The function should have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(m), where m is the number of unique elements in the resulting list.
"""

def convert_to_list(input_string):
    input_string = input_string.strip()
    
    if not input_string:
        return []
    
    elements = input_string.split(',')
    unique_elements = set([element.strip().lower() for element in elements])
    
    return list(unique_elements)