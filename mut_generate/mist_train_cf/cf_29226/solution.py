"""
QUESTION:
Implement the `process_regex` function, which takes in a list of tuples (`regex_list`) and an input string (`input_string`). Each tuple in `regex_list` contains a conversion function and a regular expression string. The function should apply each regular expression to the input string, extract the named capture groups, and return a dictionary where the keys are the named capture groups and the values are lists of corresponding matches found in the input string.
"""

import re

def process_regex(regex_list, input_string):
    result = {}
    for convert_func, regex_pattern in regex_list:
        match = re.search(regex_pattern, input_string)
        if match:
            groups = match.groupdict()
            for key, value in groups.items():
                if key in result:
                    result[key].append(value)
                else:
                    result[key] = [value]
    return result