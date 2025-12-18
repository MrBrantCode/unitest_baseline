"""
QUESTION:
Implement a function `match_pattern(strings, pattern)` that takes a list of strings and a string pattern as input, and returns a list of strings that match the given pattern. The pattern can contain two types of wildcard characters: "?" which matches any single character, and "*" which matches any sequence of characters (including an empty sequence). The function should be case-sensitive.
"""

def match_pattern(strings, pattern):
    def is_match(string, pattern):
        # Base case: if both the string and pattern are empty, they match
        if len(string) == 0 and len(pattern) == 0:
            return True
        
        # If the pattern is empty but the string is not, they don't match
        if len(pattern) == 0:
            return False
        
        # If the pattern starts with a "*", recursively check if the string
        # matches the pattern without the "*" or if the string matches the
        # pattern without the first character
        if pattern[0] == "*":
            return is_match(string, pattern[1:]) or (len(string) > 0 and is_match(string[1:], pattern))
        
        # If the pattern starts with a "?", recursively check if the string
        # matches the pattern without the "?", otherwise check if the first
        # characters of the string and pattern match, and recursively check
        # if the remaining characters match
        if pattern[0] == "?":
            return len(string) > 0 and is_match(string[1:], pattern[1:])
        
        # If the first characters of the string and pattern match, recursively
        # check if the remaining characters match
        return len(string) > 0 and string[0] == pattern[0] and is_match(string[1:], pattern[1:])
    
    result = [string for string in strings if is_match(string, pattern)]
    
    return result