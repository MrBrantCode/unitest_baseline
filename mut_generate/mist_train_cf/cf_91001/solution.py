"""
QUESTION:
Write a function `convert_string_to_list` that takes a comma-separated string as input and returns a list of unique elements. The function should remove leading and trailing spaces from the input string, handle empty strings, and ignore duplicates. The function should have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(m), where m is the number of unique elements in the resulting list.
"""

def convert_string_to_list(input_string):
    input_string = input_string.strip()  
    if not input_string:  
        return []  

    elements = input_string.split(",")  
    unique_elements = set(elements)  

    return list(unique_elements) 