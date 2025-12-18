"""
QUESTION:
Write a function named `group_strings` that takes a list of strings as input and returns a dictionary. The dictionary should have the first two characters of each string as keys and lists of strings that start with those characters as values. Do not use any built-in functions or libraries that directly solve the problem. Implement the grouping logic from scratch.
"""

def group_strings(strings):
    groups = {}
    for string in strings:
        prefix = string[:2]
        if prefix in groups:
            groups[prefix].append(string)
        else:
            groups[prefix] = [string]
    return groups