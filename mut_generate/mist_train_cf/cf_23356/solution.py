"""
QUESTION:
Write a function called `split_words` that takes a list of strings as input, splits each string into two substrings of approximately equal length, and returns a list of tuples where each tuple contains the two substrings.
"""

def split_words(string_list):
    new_list = []
    for string in string_list:
        mid = int(len(string)/2) 
        new_list.append( (string[:mid], string[mid:]) )
    return new_list