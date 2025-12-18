"""
QUESTION:
Create a function `count_chars` that takes a string as input and returns a dictionary containing the number of occurrences of each alphanumeric character and whitespace, where the keys are in ascending order of their ASCII values. The function should handle both uppercase and lowercase letters, ignore non-alphanumeric characters other than whitespace, and have a time complexity of O(n) or better.
"""

def count_chars(string):
    counts = {}
    for char in string:
        if char.isalnum() or char.isspace():
            char = char.lower() if char.isalpha() else char
            counts[char] = counts.get(char, 0) + 1
    return dict(sorted(counts.items(), key=lambda x: ord(x[0])))