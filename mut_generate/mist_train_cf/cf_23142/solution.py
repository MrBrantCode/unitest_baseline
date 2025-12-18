"""
QUESTION:
Write a function `tuple_to_dict` that takes in a tuple of strings as input and returns a dictionary where each string is a key and its corresponding value is a list of indices where the string appears in the tuple. If a string appears multiple times, its key in the dictionary should contain all of its indices. The function should have a time complexity of O(n), where n is the length of the tuple, and should not use any built-in Python functions or libraries that directly solve the problem.
"""

def tuple_to_dict(tuple_of_strings):
    result_dict = {}
    for i in range(len(tuple_of_strings)):
        string = tuple_of_strings[i]
        if string not in result_dict:
            result_dict[string] = [i]
        else:
            result_dict[string].append(i)
    return result_dict