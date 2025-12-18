"""
QUESTION:
Write a function named `substring_list` that takes a list of strings and a substring as input, and returns a list of strings that contain the given substring. The search for substrings should be case-insensitive. Implement this function using recursion and ensure that it has a time complexity of O(n*m) and a space complexity of O(n).
"""

def substring_list(strings, substring):
    def is_substring(string, substring):
        if len(substring) > len(string):
            return False
        
        for i in range(len(string)-len(substring)+1):
            if string[i:i+len(substring)].lower() == substring.lower():
                return True
        
        return False
    
    result = []
    
    for s in strings:
        if is_substring(s, substring):
            result.append(s)
    
    return result