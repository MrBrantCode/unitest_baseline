"""
QUESTION:
Implement a function `parse_json(json_str)` that takes a JSON string as input and returns the value corresponding to the key "name" where the key "id" has a value of 2. The function should implement a JSON parsing algorithm from scratch without using any existing JSON parsing libraries. The JSON string is expected to be a single-level JSON object containing an array of objects with "id" and "name" keys.
"""

def parse_json(json_str):
    tokens = []
    i = 0

    while i < len(json_str):
        char = json_str[i]

        if char.isspace():
            i += 1
            continue

        if char in ['{', '}', '[', ']', ',', ':']:
            tokens.append(char)
            i += 1
        elif char == '"':
            j = i + 1
            while j < len(json_str):
                if json_str[j] == '"' and json_str[j - 1] != '\\':
                    tokens.append(json_str[i:j + 1])
                    i = j + 1
                    break
                j += 1
        else:
            j = i
            while j < len(json_str) and json_str[j] not in ['{', '}', '[', ']', ',', ':', '"']:
                j += 1
            tokens.append(json_str[i:j])
            i = j

    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        if token == '{':
            while i < len(tokens):
                key = tokens[i].strip('"')
                if key == 'id' and tokens[i + 1] == ':' and tokens[i + 2] == '2':
                    return tokens[i + 4].strip('"')  # Assuming the value is always a string
                i += 1

        i += 1

    return None