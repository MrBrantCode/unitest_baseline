"""
QUESTION:
Create a function called `filter_strings` that takes a list of strings and a character as input, and returns a new list containing only the strings that include the given character. The function should not modify the original list.
"""

def filter_strings(my_list, character):
    return [word for word in my_list if character in word]