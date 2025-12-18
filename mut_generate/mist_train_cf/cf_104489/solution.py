"""
QUESTION:
Write a function called `adjust_strings` that takes a list of strings as input. The function should modify each string in the list to have a length of exactly 8 characters. If a string is shorter than 8 characters, append 'a' to the end until it reaches 8 characters. If a string is longer than 8 characters, truncate it to its first 8 characters. Return the modified list of strings.
"""

def adjust_strings(lst):
    adjusted_lst = []
    for string in lst:
        if len(string) < 8:
            string += 'a' * (8 - len(string))
        elif len(string) > 8:
            string = string[:8]
        adjusted_lst.append(string)
    return adjusted_lst