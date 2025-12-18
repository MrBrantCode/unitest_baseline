"""
QUESTION:
Write a function `fix_length` that takes a list of strings as input and returns a new list where all strings have a length of 5 characters. If a string has less than 5 characters, append the letter 'a' to the end until it reaches a length of 5. If a string has more than 5 characters, truncate the string to only include the first 5 characters.
"""

def fix_length(lst):
    fixed_lst = []
    for string in lst:
        if len(string) < 5:
            fixed_string = string + 'a' * (5 - len(string))
        else:
            fixed_string = string[:5]
        fixed_lst.append(fixed_string)
    return fixed_lst