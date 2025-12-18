"""
QUESTION:
Implement a function `find_matching_string` that takes in a list of strings `string_list` and a search term `search_term` containing wildcards (represented by asterisks), and returns the index of the first occurrence of the matching string. The function should return -1 if no match is found. The search term can contain multiple wildcard characters that can match different parts of the string. The time complexity should be less than O(n^2), where n is the length of the list of strings.
"""

def find_matching_string(string_list, search_term):
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