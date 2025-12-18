"""
QUESTION:
Create a Python function called `split_string` that takes a string and a delimiter as arguments and returns a list containing the string split by the delimiter with any leading or trailing whitespace removed from each split element. The function should handle cases where the delimiter appears multiple times consecutively, at the beginning or end of the string, and not found in the string. The time complexity of the function should be O(n), where n is the length of the input string.
"""

def split_string(string, delimiter):
    if not string or delimiter not in string:
        return [string.strip()] if string else []
    
    result = []
    start = 0
    length = len(string)
    
    for i in range(length):
        if string[i] == delimiter:
            if start != i:
                result.append(string[start:i].strip())
            start = i + 1
    
    if start != length:
        result.append(string[start:].strip())
    
    return result