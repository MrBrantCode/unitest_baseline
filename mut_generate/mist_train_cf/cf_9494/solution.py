"""
QUESTION:
Write a function named `group_strings` that groups a list of strings based on the first two characters of each string. The function should return a dictionary where the keys are the first two characters and the values are lists of strings that start with those characters. The input is a list of strings and the output is a dictionary. The function should handle lists of varying lengths and strings of varying lengths, but it can assume that all strings have at least two characters.
"""

def group_strings(strings):
    groups = {}
    for s in strings:
        if s[:2] in groups:
            groups[s[:2]].append(s)
        else:
            groups[s[:2]] = [s]
    return groups