"""
QUESTION:
Design a function `extract_data(s)` to parse and extract particular information from the input string `s`. The function should handle different separators (spaces, semicolons, commas) and a wide range of character types. If the string consists entirely of uppercase alphabetic characters, the function should return the count of characters at even indices. If the string contains mixed character types, the function should return a dictionary displaying the count of each character type (uppercase, lowercase, numeric, others). If the string contains any of the separators, the function should return a list of components separated by these separators.
"""

def extract_data(s):
    separators = [' ', ',', ';']
    
    if s.isupper():
        return sum(1 for c in s if (ord(c) - ord('A')) % 2 == 0)

    if any(sep in s for sep in separators):
        for sep in separators:
            s = s.replace(sep, ' ')
        return s.split()
    
    return {'upper': sum(c.isupper() for c in s),
            'lower': sum(c.islower() for c in s),
            'digits': sum(c.isdigit() for c in s),
            'others': sum(not c.isalnum() for c in s)}