"""
QUESTION:
Create a function `count_chars` that takes a string as input and returns a dictionary. The dictionary should contain the counts of each unique alphanumeric character, ignoring whitespace characters and special characters, in a case-sensitive manner. Each key in the dictionary should map to another dictionary containing the character count and a list of indices where the character appears in the string. The time complexity of the function should be O(n), where n is the length of the input string.
"""

def count_chars(input_string):
    char_counts = {}
    for i, char in enumerate(input_string):
        if char.isalnum():
            if char in char_counts:
                char_counts[char]['count'] += 1
                char_counts[char]['positions'].append(i)
            else:
                char_counts[char] = {'count': 1, 'positions': [i]}
    return char_counts