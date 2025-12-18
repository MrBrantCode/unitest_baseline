"""
QUESTION:
Implement three functions in Python: `find_pattern`, `encode_decode`, and `format_string`. 

- The `find_pattern` function should take two parameters, `text` and `pattern`, and return all non-overlapping matches of `pattern` in `text` as a list of strings using regular expression. 

- The `encode_decode` function should take two parameters, `input` and `encoding_format`, and return the decoded string after encoding the `input` string using the specified `encoding_format`.

- The `format_string` function should take two parameters, `name` and `age`, and return a formatted string in the format "My name is {} and I am {} years old.". 

Note: The functions should be able to handle any valid input and should not have any external dependencies other than the built-in Python modules.
"""

import re

def find_pattern(text, pattern):
    return re.findall(pattern, text)

def encode_decode(input, encoding_format):
    encode_text = input.encode(encoding_format)
    decode_text = encode_text.decode(encoding_format)
    return decode_text

def format_string(name, age):
    return "My name is {} and I am {} years old.".format(name, age)