"""
QUESTION:
Create a function called `split_string` that takes two arguments: a string and a delimiter. The function should split the string into a list of substrings separated by the delimiter and return the list. It should remove any leading or trailing whitespace from each substring and handle consecutive delimiters, delimiters at the beginning or end of the string, and cases where the delimiter is a substring of a word. If the input string is empty or the delimiter is not found in the string, the function should return an empty list. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def split_string(string, delimiter):
    if not string or delimiter not in string:
        return []
    
    result = []
    start = 0
    end = 0
    while end < len(string):
        if string[end:end+len(delimiter)] == delimiter:
            if start != end:
                result.append(string[start:end].strip())
            start = end + len(delimiter)
            end = start
        else:
            end += 1
    
    if start != end:
        result.append(string[start:end].strip())
    
    return result