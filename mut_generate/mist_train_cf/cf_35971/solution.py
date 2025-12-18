"""
QUESTION:
Implement the function `escape_c_string(s)` that takes a string `s` as input and returns a new string with all the special characters in C-style strings properly escaped. Special characters include newline (\n), tab (\t), backslash (\), and double quotes ("). The function should use Python and return the escaped string without enclosing double quotes.
"""

import json

def escape_c_string(s):
    return json.dumps(s)[1:-1]