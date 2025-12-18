"""
QUESTION:
Create a Python function called `split_string` that takes two arguments: `string` and `delimiter`. The function should split the input `string` by the `delimiter`, remove any leading or trailing whitespace from each split element, and return a list containing the split elements. The function should handle consecutive delimiters, delimiters at the beginning or end of the string, and cases where the delimiter is a substring of a word in the string. The function should also remove any other whitespace within the split elements. If the input string is empty or the delimiter is not found in the string, the function should return an empty list.

Constraints: 
- The input string will not exceed 10^6 characters.
- The delimiter will not exceed 10 characters.
- The input string will only contain printable ASCII characters.
"""

def split_string(string, delimiter):
    if not string or delimiter not in string:
        return []
    
    result = []
    split_parts = string.split(delimiter)
    
    for part in split_parts:
        part = part.strip()
        part = "".join(part.split())
        if part:
            result.append(part)
    
    return result