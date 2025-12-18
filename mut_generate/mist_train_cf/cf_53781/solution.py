"""
QUESTION:
Create a function `extract_data(s)` that takes a string `s` as input and returns the extracted information based on the following conditions:

- If `s` contains only upper-case alphabetic characters, return the count of characters with an even index.
- If `s` contains mixed character types, return a dictionary with the count of each character type (upper, lower, digits, others).
- Otherwise, split `s` into words separated by whitespace, semicolons, or commas and return the list of words.

Restrictions: The function should consider only the given conditions and return the corresponding output.
"""

def extract_data(s):
    s = s.replace(',', ' ').replace(';', ' ')
    
    if s.isupper():
        return sum(1 for c in s if (ord(c)-ord('A')) % 2 == 0)
    
    d = {'upper': 0, 'lower': 0, 'digits': 0, 'others': 0}
    for c in s:
        if c.isupper():
            d['upper'] += 1
        elif c.islower():
            d['lower'] += 1
        elif c.isdigit():
            d['digits'] += 1
        else:
            d['others'] += 1
            
    if all(d.values()):
        return d
    else:
        return s.split()