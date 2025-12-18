"""
QUESTION:
Implement a function `find_index` that takes in a list of strings `string_list` and a search term `search_term`, and returns the index of the first occurrence of the matching string. The search term can contain wildcards, represented by asterisks (*), which can match any number of characters (including zero). The function should have a time complexity of O(n), where n is the total number of characters in the list of strings.
"""

def find_index(string_list, search_term):
    for i, string in enumerate(string_list):
        j = 0
        k = 0
        while j < len(string) and k < len(search_term):
            if search_term[k] == '*':
                k += 1
                if k == len(search_term):
                    return i
                while j < len(string) and string[j] != search_term[k]:
                    j += 1
            elif string[j] == search_term[k]:
                j += 1
                k += 1
                if k == len(search_term):
                    return i
            else:
                k = 0
                j += 1
    return -1