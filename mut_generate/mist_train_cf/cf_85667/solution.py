"""
QUESTION:
Create a function `string_to_camelcase` that takes a string as input. If the string is a boolean ("true" or "false"), return it as is. If the string is a valid base64 string, decode it into ASCII format and then convert it to CamelCase. Otherwise, convert the input string to CamelCase directly. The function should return the resulting string.
"""

import base64
import re

def string_to_camelcase(s):
    if s.lower() == 'true' or s.lower() == 'false':
        return s
    elif re.compile(r'^[A-Za-z0-9+/]*={0,2}$').match(s):
        try:
            decoded_s = base64.b64decode(s).decode("utf-8")
            return re.sub(r"(?!^)_([a-zA-Z])", lambda m: m.group(1).upper(), decoded_s)
        except:
            pass
    return re.sub(r"(?!^)_([a-zA-Z])", lambda m: m.group(1).upper(), s)