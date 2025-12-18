"""
QUESTION:
Implement a Python decorator named `FixedWidthDecorator` that takes an integer `width` as an argument and decorates a function to format its output to the specified width. The decorator should ensure that the output is limited to the specified characters per line and return the formatted text. The decorated function should take a string `text` as input and return the formatted output.
"""

def FixedWidthDecorator(width):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            lines = [result[i:i + width] for i in range(0, len(result), width)]
            return '\n'.join(lines)
        return wrapper
    return decorator