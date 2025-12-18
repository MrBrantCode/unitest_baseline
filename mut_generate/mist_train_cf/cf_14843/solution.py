"""
QUESTION:
Write a function `parse_input` that takes a list of strings in the format 'name,age' and returns a list of dictionaries with 'name' and 'age' keys. The 'name' key should store a string and the 'age' key should store an integer.
"""

def parse_input(input_list):
    """
    This function takes a list of strings in the format 'name,age' and returns 
    a list of dictionaries with 'name' and 'age' keys.

    Args:
    input_list (list): A list of strings in the format 'name,age'

    Returns:
    list: A list of dictionaries with 'name' and 'age' keys
    """
    output_list = []
    for item in input_list:
        name, age = item.split(',')
        output_list.append({'name': name, 'age': int(age)})
    return output_list