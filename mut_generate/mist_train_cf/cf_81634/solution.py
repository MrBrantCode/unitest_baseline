"""
QUESTION:
Write a function `convert_int_list_to_string` that takes a list of integers as input and returns a string where the integers are separated by commas.
"""

def convert_int_list_to_string(integer_list):
    string_list = list(map(str, integer_list))
    return ','.join(string_list)