"""
QUESTION:
Create a function named `remove_duplicates` that takes a list of strings as input and returns a new list containing the same strings without duplicates, ignoring case sensitivity. The function should also remove any leading or trailing whitespace from each string and exclude any strings that are palindromes.
"""

def remove_duplicates(strings):
    unique_strings = []
    for string in strings:
        string = string.strip().lower()
        if string not in unique_strings and string != string[::-1]:
            unique_strings.append(string)
    return unique_strings