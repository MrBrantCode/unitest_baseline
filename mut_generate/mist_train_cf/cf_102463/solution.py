"""
QUESTION:
Implement the `sort_strings_by_length` function that takes a list of strings as input and returns a new list containing the same strings, sorted in descending order of their lengths without using any built-in sorting functions or libraries.
"""

def sort_strings_by_length(strings):
    sorted_strings = []
    
    for string in strings:
        insert_index = 0
        while insert_index < len(sorted_strings) and len(string) < len(sorted_strings[insert_index]):
            insert_index += 1
        sorted_strings.insert(insert_index, string)
    
    return sorted_strings