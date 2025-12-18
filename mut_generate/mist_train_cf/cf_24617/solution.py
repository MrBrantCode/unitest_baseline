"""
QUESTION:
Create a function called `make_length_five` that takes a list of strings as input and modifies the list so that all strings have a length of 5 characters. If a string is shorter than 5 characters, pad it with spaces. If a string is longer than 5 characters, truncate it to 5 characters.
"""

def make_length_five(lst):
    '''This function will ensure that all strings in the list have a length of 5 characters.'''
    for i in range(len(lst)):
        if len(lst[i]) < 5:
            lst[i] = lst[i] + ' ' * (5 - len(lst[i]))
        elif len(lst[i]) > 5:
            lst[i] = lst[i][:5]
    return lst