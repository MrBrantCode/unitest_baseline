"""
QUESTION:
Write a function `string_length_dict` that takes a list of strings as input and returns a dictionary. The dictionary should contain the strings as keys and their lengths as values. If a string contains numbers or special characters, it should be ignored. If there are duplicate strings in the input list, only the length of the first occurrence of each string should be included in the dictionary.
"""

def string_length_dict(strings):
    length_dict = {}
    for string in strings:
        if any(char.isdigit() or not char.isalnum() for char in string):
            continue
        if string not in length_dict:
            length_dict[string] = len(string)
    return length_dict