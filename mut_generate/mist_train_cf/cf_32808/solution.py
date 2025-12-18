"""
QUESTION:
Implement a function `to_percent(obj, significant_digits)` that converts a numerical value `obj` into a percentage format with a specified number of `significant_digits`. The function should return a string representing the percentage value rounded to the specified number of significant digits and including the percentage symbol (%). If `obj` is not a valid numerical value or is None, the function should return an empty string.
"""

def to_percent(obj, significant_digits):
    if obj is None:
        return ""
    try:
        value = float(obj) * 100  # Convert to percentage
        format_str = "{:.%df}%%" % significant_digits  # Create format string with specified significant digits
        return format_str.format(value)  # Format the value as percentage with specified significant digits
    except (ValueError, TypeError):
        return ""