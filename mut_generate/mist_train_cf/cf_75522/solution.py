"""
QUESTION:
Create a function called `extract_data` that takes a string as input. The function should return a list of words split by either a blank space, semicolon, or comma. If the string consists only of uppercase alphabetic letters, return the count of letters with an even index (0-indexed from 'A' to 'Z'). If the string contains a mixture of character types, return a dictionary with the quantity count of each character class: uppercase letters, lowercase letters, numerical digits, and other types.
"""

def extract_data(s):
    if ',' in s: 
        return s.split(',')
    if ';' in s: 
        return s.split(';')
    if s.isupper(): 
        return sum([1 for c in s if (ord(c) - ord('A')) % 2 == 0])
    elif ' ' in s: 
        return s.split()
    
    counts = {'upper': 0,'lower': 0, 'digits': 0, 'others': 0}
    for c in s:
        if c.isupper():
            counts['upper'] += 1
        elif c.islower():
            counts['lower'] += 1
        elif c.isdigit():
            counts['digits'] += 1
        else:
            counts['others'] += 1
    
    return counts