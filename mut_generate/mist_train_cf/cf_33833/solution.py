"""
QUESTION:
Implement a class method `format_string` for the `IndentationFormatter` class. The method should take two parameters: `pre` (the string to be formatted) and an optional parameter `auto_break` (default is `False`). The method should return the `pre` string indented with `self.i` number of tab characters (`\t`). If `auto_break` is `True`, a line break character (`\n`) should be appended to the end of the formatted string.
"""

def format_string(pre, auto_break=False):
    indent = i * '\t' + pre
    if auto_break:
        return indent + '\n'
    else:
        return indent