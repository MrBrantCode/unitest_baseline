"""
QUESTION:
Implement a recursive function `find_substrings` that takes a list of strings `string_list` and a string `sub_string` as inputs. 

The function should find all the strings in `string_list` that contain `sub_string`, ignoring special characters and case sensitivity. It should also count the number of occurrences of `sub_string` in each matching string. 

If no strings in `string_list` contain `sub_string`, the function should return 'No matches found.' Otherwise, it should return a dictionary with each matching string as a key and the count of `sub_string` occurrences as the value. 

The function should handle overlapping occurrences of `sub_string` in the same string.
"""

import re

def find_substrings(string_list, sub_string):
    result = {}
    for word in string_list:
        count = 0
        cleaned_word = re.sub(r'\W+', '', word).lower()
        sub_str = sub_string.lower()
        pos = cleaned_word.find(sub_str)
        while pos != -1:
            count += 1
            pos = cleaned_word.find(sub_str, pos+1)
        if count > 0:
            result[word] = count
    return 'No matches found.' if not result else result