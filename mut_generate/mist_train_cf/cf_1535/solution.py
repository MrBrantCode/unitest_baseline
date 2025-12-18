"""
QUESTION:
Write a function `count_substring_occurrences` that counts the occurrences of a given substring in a string, ignoring any occurrences that are part of a larger word. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1). The function should also handle case-insensitive matching and not use any built-in string functions or regular expressions.
"""

def count_substring_occurrences(string, substring):
    count = 0
    len_string = len(string)
    len_substring = len(substring)
    
    i = 0
    while i <= len_string - len_substring:
        j = 0
        while j < len_substring:
            if string[i+j].lower() != substring[j].lower():
                break
            j += 1
        if j == len_substring:
            if (i == 0 or not string[i-1].isalpha()) and (i+len_substring == len_string or not string[i+len_substring].isalpha()):
                count += 1
            i += len_substring
        else:
            i += 1
    
    return count