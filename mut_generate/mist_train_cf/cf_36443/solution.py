"""
QUESTION:
Implement a function named `parse_key_value` that takes an input string in the format "key1=value1,key2=value2,key3=value3,...", where each key-value pair is separated by a comma and keys and values are separated by an equal sign. The function should extract the key-value pairs from the input string and return them as a dictionary. If the input string is not in the correct format, the function should raise an exception with an appropriate error message. Keys and values can contain any characters except for the comma, and the function should handle escaped characters.
"""

class InvalidArgument(Exception):
    pass

def parse_key_value(input_string):
    key_value_map = {}
    cur_key = ""
    cur_val = ""
    reading_key = True
    escaped = False

    for c in input_string:
        if c == '=' and not escaped:
            if cur_key == "":
                raise InvalidArgument("Bad KV spec empty key")
            reading_key = False
        elif c == ',' and not escaped:
            if cur_key == "":
                raise InvalidArgument("Bad KV spec empty key")
            if cur_key in key_value_map:
                raise InvalidArgument("Bad KV spec duplicated key")
            key_value_map[cur_key] = cur_val
            cur_key = ""
            cur_val = ""
            reading_key = True
        elif c == '\\':
            escaped = True
        else:
            if reading_key:
                cur_key += c
            else:
                cur_val += c
            escaped = False

    if cur_key == "":
        raise InvalidArgument("Bad KV spec empty key")
    if cur_key in key_value_map:
        raise InvalidArgument("Bad KV spec duplicated key")
    key_value_map[cur_key] = cur_val

    return key_value_map