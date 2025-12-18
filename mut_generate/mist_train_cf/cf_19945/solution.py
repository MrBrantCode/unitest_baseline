"""
QUESTION:
Write a function called `convert_list_to_dict` that takes a list of strings as input, removes any duplicate strings, and returns a dictionary where the keys are the unique strings and the values are the lengths of the strings. The function must have a time complexity of O(n), where n is the length of the input list, and must not use any built-in functions or methods that directly convert a list into a dictionary or remove duplicate elements from a list.
"""

def convert_list_to_dict(lst):
    unique_lst = []
    for string in lst:
        if string not in unique_lst:
            unique_lst.append(string)
    dictionary = {}
    for string in unique_lst:
        dictionary[string] = len(string)
    return dictionary