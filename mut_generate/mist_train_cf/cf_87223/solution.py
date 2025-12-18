"""
QUESTION:
Implement the function `count_substring_occurrences(string, substring)` to find the number of non-overlapping occurrences of `substring` in `string`. The function should be case-sensitive and account for leading and trailing whitespace characters in both `string` and `substring`. The `substring` must have a length between 3 and 20 characters, and can contain alphanumeric characters, punctuation, and special symbols. If `substring` is empty or longer than `string`, return -1.
"""

def count_substring_occurrences(string, substring):
    if not substring or len(substring) < 3 or len(substring) > 20 or len(substring) > len(string):
        return -1
    
    count = 0
    normalized_string = string.strip()  
    normalized_substring = substring.strip()  
    
    for i in range(len(normalized_string) - len(normalized_substring) + 1):
        if normalized_string[i:i+len(normalized_substring)] == normalized_substring:
            count += 1
    
    return count