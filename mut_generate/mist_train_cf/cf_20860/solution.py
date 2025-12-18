"""
QUESTION:
Write a function named `find_control_characters` that takes a string as input. This function should return two dictionaries, one containing the count of each type of control character (carriage returns, line feeds, tabs, and non-printable ASCII characters) and another containing their respective positions in the string. Non-printable ASCII characters are those with ASCII values less than 32, excluding carriage returns, line feeds, and tabs. The function should handle cases with multiple occurrences of the same control character or non-printable ASCII character and correctly identify their positions. It should also handle edge cases such as an empty string or a string that contains no control characters or non-printable ASCII characters.
"""

def find_control_characters(string):
    control_characters = {
        '\r': 'Carriage returns',
        '\n': 'Line feeds',
        '\t': 'Tabs'
    }
    
    counts = {
        'Carriage returns': 0,
        'Line feeds': 0,
        'Tabs': 0,
        'Non-printable ASCII characters': 0
    }
    
    positions = {
        'Carriage returns': [],
        'Line feeds': [],
        'Tabs': [],
        'Non-printable ASCII characters': []
    }
    
    for i, char in enumerate(string):
        if char in control_characters:
            counts[control_characters[char]] += 1
            positions[control_characters[char]].append(i)
        elif ord(char) < 32:
            counts['Non-printable ASCII characters'] += 1
            positions['Non-printable ASCII characters'].append(i)
    
    return counts, positions