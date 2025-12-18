"""
QUESTION:
Implement a function `find_index(string_list, search_term)` that takes a list of strings `string_list` and a search term `search_term` as input. The function should return the index of the first occurrence of the matching string in the list. The search term may contain wildcards, represented by asterisks (*), which can match any number of characters (including zero). If no match is found, the function should return -1. The time complexity of the solution should be O(n), where n is the total number of characters in the list of strings.
"""

def find_index(string_list, search_term):
    for i, string in enumerate(string_list):
        j = 0
        k = 0
        while j < len(string) and k < len(search_term):
            if search_term[k] == '*':
                # Handle wildcard case
                k += 1
                if k == len(search_term):
                    return i
                while j < len(string) and string[j] != search_term[k]:
                    j += 1
            elif string[j] == search_term[k]:
                # Handle exact match case
                j += 1
                k += 1
                if k == len(search_term):
                    return i
            else:
                # No match, reset to start of search term
                k = 0
                j += 1
    return -1