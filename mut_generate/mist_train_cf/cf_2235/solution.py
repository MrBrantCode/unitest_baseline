"""
QUESTION:
Implement a function `last_occurrence_recursive(string, substring)` that uses recursion to find the index of the last occurrence of a case-insensitive substring in a given string, ignoring leading and trailing whitespaces in both strings. The function should handle empty substrings by returning the index of the last character in the given string and return -1 if the substring is not found.
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