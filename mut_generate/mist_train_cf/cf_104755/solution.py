"""
QUESTION:
Create a function named `replace_character` that takes a string as input and returns a modified string. If the input string's length is greater than 5, the function should replace all lowercase 'e's with uppercase 'E's; otherwise, it should return the original string. The function should also count the total occurrences of lowercase 'e' in the string, regardless of its length, and append this count in the format "(X e)" to the end of the modified string, where X is the count of 'e'. The function should be case-sensitive.
"""

def replace_character(s):
    count = s.count('e')
    if len(s) > 5:
        s = s.replace('e', 'E')
    return f"{s} ({count} e)"