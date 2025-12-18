"""
QUESTION:
Create a function `my_solution` that takes a list of strings as input, replaces all occurrences of the word "right" with "left" and vice versa in each string, and then returns the modified strings concatenated with commas. The replacement should be case-sensitive and only replace the exact word "right" or "left", not parts of other words.
"""

def entrance(strings):
    modified_strings = []
    for s in strings:
        modified_s = s.replace('right', 'temp').replace('left', 'right').replace('temp', 'left')
        modified_strings.append(modified_s)
    return ','.join(modified_strings)