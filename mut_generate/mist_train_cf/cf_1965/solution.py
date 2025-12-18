"""
QUESTION:
Implement a function called `count_substring_occurrences` that takes two parameters: `string` and `substring`. The function should count the number of non-overlapping occurrences of the substring in the string, where the substring has a length between 3 and 20 characters and can contain alphanumeric characters, punctuation, and special symbols. The function should be case-sensitive and account for leading and trailing whitespace characters. If the substring is empty or longer than the string, return -1. The string can have a maximum length of 10^7 characters and can contain any printable ASCII characters.
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