"""
QUESTION:
Create a function `count_chars` that takes a string of text as input and returns a dictionary containing the number of occurrences of each alphanumeric character (both uppercase and lowercase) and whitespace character in the string. The output dictionary should be sorted in ascending order of the characters' ASCII values. Non-alphanumeric characters other than whitespace characters should not be included in the output dictionary. The function should handle long strings efficiently with a time complexity of O(n) or better.
"""

def count_chars(text):
    counts = {}
    for char in text:
        if char.isalnum() or char.isspace():
            char = char.lower() if char.isalnum() else char
            counts[char] = counts.get(char, 0) + 1
    return dict(sorted(counts.items(), key=lambda x: ord(x[0])))