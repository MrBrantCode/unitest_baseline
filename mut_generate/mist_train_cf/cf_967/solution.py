"""
QUESTION:
Write a function `find_substring_index(string, substring)` that finds the first index of the substring in the string. The function should be case-insensitive and should not use any built-in string search functions or regular expressions. The time complexity requirement is O(n) and the space complexity requirement is O(1), where n is the length of the string.
"""

def find_substring_index(string, substring):
    # Convert the string and substring to lowercase
    string = string.lower()
    substring = substring.lower()
    
    # Initialize the window start and end indices
    start = 0
    end = len(substring)
    
    while end <= len(string):
        # Check if the substring matches the current window
        if string[start:end] == substring:
            return start
        
        # Slide the window by 1 position
        start += 1
        end += 1
    
    # If the substring is not found, return -1
    return -1