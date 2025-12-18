"""
QUESTION:
Function: split_string
Information: This function splits a given string into a list of substrings using any special characters or digits present in the string as delimiters. The function handles consecutive delimiters, empty substrings, and ignores any delimiters within quotes (both single and double quotes). The resulting list includes the substrings between the delimiters, as well as the delimiters themselves.
Restriction: The time complexity should be O(n) and the space complexity should be O(n), where n is the length of the input string.
"""

def entrance(string):
    substrings = []
    delimiter = ''
    in_quotes = False

    for char in string:
        if char in ('\'', '\"'):
            in_quotes = not in_quotes
            delimiter += char
        elif in_quotes:
            delimiter += char
        elif char.isalnum():
            delimiter += char
        else:
            if delimiter:
                substrings.append(delimiter)
                delimiter = ''
            substrings.append(char)
    
    if delimiter:
        substrings.append(delimiter)
    
    return substrings