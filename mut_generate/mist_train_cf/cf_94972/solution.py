"""
QUESTION:
Combine the strings in a given array into a single string, following these rules: 
1. Only include strings with both uppercase and lowercase letters.
2. Ignore strings with special characters or numbers.
3. Sort the included strings in descending order of their lengths before combining them.
4. If no strings meet the requirements, return an empty string.

The input array will contain at most 1000 strings, each with at most 100 characters. Implement the function `combine_strings(array)`.
"""

def entrance(array):
    valid_strings = [string for string in array 
                     if string.isalpha() and 
                     any(char.isupper() for char in string) and 
                     any(char.islower() for char in string)]
    
    return ''.join(sorted(valid_strings, key=len, reverse=True))