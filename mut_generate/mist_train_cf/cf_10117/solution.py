"""
QUESTION:
Create a function `sort_strings(strings, alphabet)` that sorts a list of strings `strings` based on a given alphabetical order defined by a dictionary `alphabet`. The sorting should be performed in a way that the strings are arranged in ascending order based on the sum of the integer values of the characters in each string. If two strings have the same sum, they should be sorted based on their length in descending order. If two strings have the same sum and length, they should be sorted in lexicographical order. The strings in the list can contain any printable ASCII characters. The function should return the sorted list of strings.
"""

def sort_strings(strings, alphabet):
    def key_func(string):
        sum_value = sum(alphabet.get(char, 0) for char in string)
        return (sum_value, -len(string), string)
    
    sorted_strings = sorted(strings, key=key_func)
    
    return sorted_strings