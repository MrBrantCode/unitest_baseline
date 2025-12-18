"""
QUESTION:
Write a function `sort_strings` that takes a list of strings as input. This function should first capitalize the first letter of each word within each string, while ignoring special characters. Then, it should sort the strings in descending order based on the number of words present in each string. The function should return the sorted list of strings.
"""

def sort_strings(strings):
    return sorted([' '.join(word.capitalize() for word in string.split()) for string in strings], key=lambda string: len(string.split()), reverse=True)