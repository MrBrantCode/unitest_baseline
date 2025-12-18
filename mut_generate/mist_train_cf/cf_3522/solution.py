"""
QUESTION:
Create a function called `parse_string` that takes a string as input. The string contains lines of key/value pairs separated by an equal sign ('='). Return a dictionary where the keys are the keys from the string and the values are the corresponding values. The keys should be case-sensitive, and in the case of duplicate keys, the value associated with the last occurrence of the key should be stored in the dictionary. 

The function should ignore leading or trailing spaces on each line, empty lines, and lines without an equal sign ('=') separating the key and value. It should also handle keys and values that contain alphanumeric characters, special characters, spaces, escape characters (such as "\n" or "\t"), and are enclosed in quotes.
"""

def parse_string(string):
    result = {}
    for line in string.split('\n'):
        if '=' in line:
            key_value = line.split('=')
            key = key_value[0].strip()
            value = key_value[1].strip()

            if key.startswith('"') and key.endswith('"'):
                key = key[1:-1]

            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]

            result[key] = value

    return result