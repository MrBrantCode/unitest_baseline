"""
QUESTION:
Write a function `sort_strings` that takes a list of strings as input. The function should capitalize the first letter of each word within each string, ignoring special characters, and then sort the strings in descending order based on the number of words present in each string. The function should return the sorted list of strings.
"""

def sort_strings(strings):
    def capitalize_words(string):
        return ' '.join(word.capitalize() for word in string.split())
    
    return sorted([capitalize_words(string) for string in strings], key=lambda string: len(string.split()), reverse=True)