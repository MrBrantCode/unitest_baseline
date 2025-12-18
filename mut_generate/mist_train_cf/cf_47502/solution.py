"""
QUESTION:
Design a function called `extract_data` that takes a string `s` as input. The function should handle strings with diverse separators (whitespace, semi-colons, commas) and variants of characters. If the string contains only capital alphabetic characters, the function should return the sum of the characters with even indices. If the string contains mixed character types, the function should return a dictionary with the count of each character variant (upper, lower, digits, others). If the string contains only separators, the function should return a list of words split by the separators.
"""

def extract_data(s):
    if s.isupper():
        return sum(1 for i in s if (ord(i) - ord('A')) % 2 == 0)

    data = {
        'upper': 0,
        'lower': 0,
        'digits': 0,
        'others': 0,
    }

    for i in s:
        if i.isupper():
            data['upper'] += 1
        elif i.islower():
            data['lower'] += 1
        elif i.isdigit():
            data['digits'] += 1
        else:
            data['others'] += 1

    if data['upper'] > 0 or data['lower'] > 0 or data['digits'] > 0 or data['others'] > 0:
        return data
    else:    
        return [i for i in s.replace(';', ' ').replace(',', ' ').split() if i]