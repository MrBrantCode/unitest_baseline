"""
QUESTION:
Create a function `toggle_case` that takes a string as input and returns a new string with the casing of each character (including white spaces and special characters) alternated, while ignoring the original case of numbers and punctuation. The function should start with the first character in uppercase.
"""

def toggle_case(text):
    result = ''
    make_upper = True
    for char in text:
        if make_upper:
            result += char.upper()
            make_upper = False
        else:            
            result += char.lower()
            make_upper = True
    return result