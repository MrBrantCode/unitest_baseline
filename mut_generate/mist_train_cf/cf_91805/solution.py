"""
QUESTION:
Create a function `parse_string(input_string)` that takes a string of key-value pairs, one pair per line, and returns a dictionary where each key is paired with its corresponding value. The function should be case-sensitive, ignore leading and trailing spaces on each line, and handle duplicate keys by storing the last occurrence's value. It should also ignore empty lines and lines without an equal sign separating the key and value. The keys and values can contain alphanumeric characters and special characters.
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