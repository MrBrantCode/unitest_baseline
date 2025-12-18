"""
QUESTION:
Create a function named `find_common_characters` that takes two strings `string1` and `string2` as input and returns a dictionary where the keys are the common characters between the two strings and the values are the minimum number of occurrences of that character in both strings. The function should handle cases where there are multiple occurrences of a character in a string.
"""

def find_common_characters(string1, string2):
    common_chars = {}
    
    # Count the occurrences of characters in string1
    for char in string1:
        if char in common_chars:
            common_chars[char] += 1
        else:
            common_chars[char] = 1
    
    # Count the occurrences of characters in string2
    string2_count = {}
    for char in string2:
        if char in string2_count:
            string2_count[char] += 1
        else:
            string2_count[char] = 1
    
    # Update the count for common characters
    common_chars = {k: min(common_chars[k], string2_count[k]) for k in common_chars if k in string2_count}
    
    return common_chars