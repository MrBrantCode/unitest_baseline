"""
QUESTION:
Create a function `is_reverse_ordered` that takes a list of strings as input. The function should check if the list is ordered lexicographically in reverse order, considering only the last two characters of each string. If a string has less than two characters, it should be considered as 'zz'.
"""

def is_reverse_ordered(list_of_strings):
    def get_last_two_chars(s):
        if len(s) < 2:
            return 'zz'
        return s[-2:]
    
    return sorted(list_of_strings, key=get_last_two_chars, reverse=True) == list_of_strings