"""
QUESTION:
Implement a function `process_regex(regex: str) -> str` that takes a regular expression string as input and returns the modified regular expression string. The function should replace substrings enclosed in curly braces `{}` with a corresponding regex pattern if the substring matches a predefined property. If the substring does not match a predefined property, it should be left unchanged. The predefined properties and their corresponding regex patterns are: `digit` maps to `\d`, and `word` maps to `\w`. The function should handle escape characters and named capturing groups.
"""

import re

def process_regex(regex: str) -> str:
    IS_PROPERTY_RE = re.compile(r'^\w+$')
    PROPERTIES = {
        'digit': r'\d',
        'word': r'\w'
    }

    processed_regex = ''
    escape = False
    in_repl = False
    repl = ''

    for c in regex:
        if escape:
            processed_regex = processed_regex + '\\' + c
            escape = False
        else:
            if c == '\\':
                escape = True
            elif c == '{':
                in_repl = True
                repl = ''
            elif c == '}':
                in_repl = False
                if IS_PROPERTY_RE.match(repl) and repl in PROPERTIES:
                    # Replace value
                    processed_regex = processed_regex + PROPERTIES[repl]
                else:
                    processed_regex = processed_regex + '{' + repl + '}'
            elif in_repl:
                repl = repl + c
            else:
                processed_regex = processed_regex + c

    return processed_regex