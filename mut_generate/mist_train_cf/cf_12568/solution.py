"""
QUESTION:
Write a function called `check_strings` that takes a list of strings as input and checks whether all strings in the list are of equal length. The function should return a message stating whether the list is empty or whether all strings in the list are of equal length.
"""

def check_strings(list_of_strings):
    if not list_of_strings:  
        return "The list is empty."
    else:
        string_length = len(list_of_strings[0])
        all_equal_length = all(len(string) == string_length for string in list_of_strings)
        if all_equal_length:
            return "All strings in the list are of equal length."
        else:
            return "Not all strings in the list are of equal length."