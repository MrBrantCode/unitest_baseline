"""
QUESTION:
Create a function `find_substrings` that takes a list of strings (`string_list`), a substring (`sub_string`), and an optional boolean parameter (`case_sensitive`) that defaults to `True`. The function should return a list of all strings in `string_list` that contain `sub_string`, considering case sensitivity based on the `case_sensitive` parameter. If `string_list` is empty, return 'No strings to search.' If `sub_string` is empty, return 'No substring provided.' If no matches are found, return 'No matches found.'
"""

def find_substrings(string_list, sub_string, case_sensitive=True):
    # dealing with edge cases
    if len(string_list) == 0:
        return 'No strings to search.'
    if len(sub_string) == 0:
        return 'No substring provided.'
  
    # initialising empty result list
    result = []

    for string in string_list:

        if case_sensitive:
            if sub_string in string:
                result.append(string)

        else:
            if sub_string.lower() in string.lower():
                result.append(string)

    if len(result) == 0:
        return 'No matches found.'
    else:
        return result