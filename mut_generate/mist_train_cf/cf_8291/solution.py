"""
QUESTION:
Create a function called `count_chars` that takes a string as input and returns a dictionary. The dictionary should contain the counts of each unique character (ignoring whitespace characters and special characters, and considering lowercase and uppercase characters as different characters) and their positions in the string as a list of indices in ascending order. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def count_chars(input_string):
    char_counts = {}
    for i, char in enumerate(input_string):
        if char.isalpha() and not char.isspace():
            if char in char_counts:
                char_counts[char]['count'] += 1
                char_counts[char]['positions'].append(i)
            else:
                char_counts[char] = {'count': 1, 'positions': [i]}
    return char_counts