"""
QUESTION:
Create a function `parse_string(input_string)` to parse a string of key/value pairs, one pair per line, separated by an equal sign ('='). The function should return a dictionary where the keys are case-sensitive and the last occurrence of a key overwrites any previous occurrences. The input string may contain leading or trailing spaces, empty lines, and lines without an equal sign, all of which should be ignored. Keys and values can contain alphanumeric characters and special characters.
"""

def parse_string(input_string):
    result = {}
    lines = input_string.split('\n')
    
    for line in lines:
        line = line.strip()
        if line == '':
            continue
        
        parts = line.split('=')
        if len(parts) != 2:
            continue
        
        key, value = parts[0], parts[1]
        result[key] = value
    
    return result