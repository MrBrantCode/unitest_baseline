"""
QUESTION:
Write a function `unique_alpha_entities(string)` that checks if a given string contains unique, non-repeated alphabetic characters only. The function should ignore non-alphabet characters and case differences. It should return a message indicating whether the string has unique, non-repeated alphabetic characters or not.
"""

def unique_alpha_entities(string):
    # Remove non-alphabet characters
    cleaned_string = ''.join(ch for ch in string if ch.isalpha())
    # Change all letters to lowercase to ignore case difference
    cleaned_string = cleaned_string.lower()
    # Set only allows unique elements, compare its length with string
    if len(cleaned_string) == len(set(cleaned_string)):
        return "The string has unique, non-repeated alphabetic characters."
    else:
        return "The string does not have unique, non-repeated alphabetic characters."