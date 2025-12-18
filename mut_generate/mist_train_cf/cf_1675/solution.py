"""
QUESTION:
Write a function `is_reverse_lexicographic` that takes a list of strings as input and checks if it is ordered lexicographically in reverse order, considering only the last two characters of each string. If a string has less than two characters, it should be considered as 'zz'. The function should have a time complexity of O(nlogn), where n is the length of the input list.
"""

def is_reverse_lexicographic(strings):
    def get_last_two_chars(string):
        if len(string) < 2:
            return 'zz'
        return string[-2:]
    sorted_strings = sorted(strings, key=lambda x: get_last_two_chars(x), reverse=True)
    return sorted_strings == strings