"""
QUESTION:
Create a function `concatenate_strings` that takes a list of strings as input, and returns a string containing all unique characters from the input strings in lexicographic order. The input list can contain duplicate strings and each string can have up to 10^6 characters. The function should have a time complexity of O(NlogN) and space complexity of O(N), where N is the total number of characters in all the strings combined.
"""

def concatenate_strings(strings):
    unique_chars = set()
    for string in strings:
        for char in string:
            unique_chars.add(char)
    sorted_chars = sorted(unique_chars)
    return ''.join(sorted_chars)