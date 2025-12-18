"""
QUESTION:
Create a function `longest_palindromic_string(strings)` that takes a nested list of strings as input. The function should return the longest palindromic string from the list, where a palindromic string is a string that reads the same forwards and backwards. If there are multiple longest palindromic strings, return the last one found in the list. If the list is empty or no palindromic string is found, return None.
"""

from typing import List, Optional, Any

def longest_palindromic_string(strings: List[Any]) -> Optional[str]:
    def flatten(lst):
        for el in lst:
            if isinstance(el, list):
                yield from flatten(el)
            else:
                yield el
    flat_list = list(flatten(strings))
    
    longest_palindromic = ''
    for string in flat_list:
        if string == string[::-1] and len(string) >= len(longest_palindromic):
            longest_palindromic = string

    return longest_palindromic if longest_palindromic != '' else None