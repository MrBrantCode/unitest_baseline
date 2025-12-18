"""
QUESTION:
Write a function `capitalize_words` that takes a string as input, splits it into individual words, capitalizes the first letter of each word, and then joins them back together with a space in between. Then, write a function `handle_list_of_strings` that uses a list comprehension to apply the `capitalize_words` function to each string in a given list and returns the modified list. The function should handle lists of any size.
"""

def capitalize_words(string):
    return ' '.join(word.capitalize() for word in string.split())

def handle_list_of_strings(string_list):
    return [capitalize_words(string) for string in string_list]