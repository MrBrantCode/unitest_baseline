"""
QUESTION:
Create a function named `find_unique_strings` that takes a list of strings as input and returns a list of strings that occur exactly once in the given list.
"""

def find_unique_strings(string_list):
    string_count = {}
    for string in string_list:
        if string not in string_count:
            string_count[string] = 1
        else:
            string_count[string] += 1
    
    unique_strings = []
    for string, count in string_count.items():
        if count == 1:
            unique_strings.append(string)
    
    return unique_strings