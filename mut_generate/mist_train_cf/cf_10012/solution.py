"""
QUESTION:
Write a function called count_occurrences(str1, str2) that takes two strings as input and returns the total number of occurrences of str2 in str1, considering overlapping occurrences. The function should handle strings of any length and content. The function should be case sensitive.
"""

def count_occurrences(str1, str2):
    count = 0
    index = 0
    
    while index < len(str1):
        if str1[index:index+len(str2)] == str2:
            count += 1
            index += len(str2) - 1
        index += 1
    
    return count