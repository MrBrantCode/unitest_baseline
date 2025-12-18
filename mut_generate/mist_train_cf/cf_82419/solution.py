"""
QUESTION:
Write a function named `filter_strings` that takes two parameters: a list of strings (`string_list`) and an integer (`length`). The function should return a list of strings from `string_list` that have a length greater than `length` and contain at least one vowel ('a', 'e', 'i', 'o', or 'u'), in a case-insensitive manner. The returned list should be sorted in lexicographical order.
"""

def filter_strings(string_list, length):
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Filter based on length and vowel condition
    filtered_list = [s for s in string_list if len(s) > length and any(char in vowels for char in s.lower())]

    # Sort the list in lexicographical order
    filtered_list.sort()
    
    return filtered_list