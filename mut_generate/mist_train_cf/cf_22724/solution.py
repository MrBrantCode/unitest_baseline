"""
QUESTION:
Create a function called `count_characters` that takes a string as input and returns a dictionary containing the count and positions of each unique alphanumeric character in the string. The function should be case-sensitive, exclude whitespace characters and special characters, and handle strings of any length. The dictionary should have characters as keys and a dictionary with 'count' and 'positions' as values, where 'count' is the number of occurrences of the character and 'positions' is a list of indices where the character appears in the string.
"""

def count_characters(string):
    counts = {}
    
    for i, char in enumerate(string):
        if char.isalnum() and not char.isspace():
            if char not in counts:
                counts[char] = {
                    'count': 1,
                    'positions': [i]
                }
            else:
                counts[char]['count'] += 1
                counts[char]['positions'].append(i)
    
    return counts