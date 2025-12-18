"""
QUESTION:
Create a function named `extract_data` that takes a string as input. The function should return a list of words separated by either whitespace or semicolon if either of these separators is present in the string. If neither separator is present, the function should return the count of uppercase alphabetic characters in the string that have an even index (where 'A' has an index of 0, 'B' has an index of 1, and so on).
"""

def extract_data(str):
    if ' ' in str:
        return str.split()
    elif ';' in str:
        return str.split(';')
    else:
        return sum([(ord(ch) - ord('A')) % 2 == 0 for ch in str if ch.isupper()])