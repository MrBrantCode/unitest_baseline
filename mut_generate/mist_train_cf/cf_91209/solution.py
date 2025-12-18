"""
QUESTION:
Create a function called `sort_strings` that takes a list of strings and an alphabet dictionary as input. The alphabet dictionary maps each letter to a unique integer value. The function should return the sorted list of strings. The sorting should be performed in ascending order based on the sum of the integer values of the characters in each string. If two strings have the same sum, they should be sorted based on their length in descending order. If two strings have the same sum and length, they should be sorted in lexicographical order. The strings in the list can contain any printable ASCII characters.
"""

def sort_strings(strings, alphabet):
    def key_func(string):
        sum_value = sum(alphabet.get(char, 0) for char in string)
        return (sum_value, -len(string), string)
    
    sorted_strings = sorted(strings, key=key_func)
    return sorted_strings