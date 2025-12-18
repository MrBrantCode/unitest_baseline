"""
QUESTION:
Create a recursive function `last_occurrence_recursive(string, substring)` to find the last occurrence of a case-insensitive substring in a given string and return the index of its starting position. The function should ignore any leading and trailing whitespaces in both the substring and the string. If the substring is empty, return the index of the last character of the given string. If the substring is not found, return -1.
"""

def last_occurrence_recursive(string, substring):
    # Remove leading and trailing whitespaces
    string = string.strip()
    substring = substring.strip()
    
    if substring == '':
        return len(string) - 1
    
    if len(substring) > len(string):
        return -1
    
    string = string.lower()
    substring = substring.lower()
    
    if string[-1] == substring[-1]:
        if string[-len(substring):] == substring:
            return len(string) - len(substring)
    
    if len(string) > 1:
        result = last_occurrence_recursive(string[:-1], substring)
        if result != -1:
            return result
    
    return -1