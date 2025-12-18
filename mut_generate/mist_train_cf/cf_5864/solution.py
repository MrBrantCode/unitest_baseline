"""
QUESTION:
Implement a function `find_matching_string(string_list, search_term)` that takes in a list of strings and a search term containing asterisks (*) as wildcards. The function should return the index of the first occurrence of the matching string in the list. The wildcards can match any number of characters, including zero, and the search term may contain multiple wildcards. Return -1 if no match is found. The time complexity of the solution should be less than O(n^2), where n is the length of the list of strings. Built-in functions for string matching are allowed, but not for regular expressions.
"""

def entrance(string_list, search_term):
    search_parts = search_term.split('*')
    for i, string in enumerate(string_list):
        index = 0
        for part in search_parts:
            index = string.find(part, index)
            if index == -1:
                break
            index += len(part)
        if index != -1:
            return i
    return -1