"""
QUESTION:
Implement a function `find_string_index` that takes in a list of strings `string_list` and a search term `search_term`, and returns the index of the first occurrence of the matching string. The search term may contain wildcard characters represented by asterisks (*), which can match any number of characters (including zero). If no match is found, return -1.
"""

def find_string_index(string_list, search_term):
    def is_matching_string(string, search_term):
        if not string and not search_term:
            return True
        if search_term and search_term[0] == "*":
            return is_matching_string(string, search_term[1:]) or (string and is_matching_string(string[1:], search_term))
        return string and search_term and string[0] == search_term[0] and is_matching_string(string[1:], search_term[1:])

    for i, string in enumerate(string_list):
        if is_matching_string(string, search_term):
            return i
    return -1