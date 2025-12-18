"""
QUESTION:
Write a function `reverse_list_of_strings` that takes a list of strings as input and returns a new list with each string reversed individually, and then the entire list reversed.
"""

def reverse_list_of_strings(strings):
    reversed_strings = []
    for string in strings:
        reversed_string = string[::-1]
        reversed_strings.append(reversed_string)
    reversed_list = reversed(reversed_strings)
    return list(reversed_list)