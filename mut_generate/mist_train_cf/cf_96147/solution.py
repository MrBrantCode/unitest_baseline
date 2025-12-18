"""
QUESTION:
Create a function named `count_distinct_characters` that takes a string as input and returns a tuple containing the total number of distinct characters in the string (excluding whitespace) and a list of these distinct characters in the order of their first occurrence.
"""

def count_distinct_characters(text):
    distinct_characters = []
    for char in text:
        if char not in distinct_characters and char != " ":
            distinct_characters.append(char)
    return len(distinct_characters), distinct_characters