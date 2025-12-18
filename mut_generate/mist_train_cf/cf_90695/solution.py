"""
QUESTION:
Write a function named `replace_substring` that takes three parameters: `string`, `substring`, and `replacement`. The function should replace all occurrences of `substring` in `string` with `replacement` in a case-insensitive manner, without using built-in string manipulation methods or regular expressions. It should handle edge cases, such as an empty `substring` or a `replacement` string longer than the original `substring`. The function should return both the modified string and the number of replacements made.
"""

def replace_substring(string, substring, replacement):
    modified_string = ""
    replacements_made = 0
    
    if substring == "":
        return string, replacements_made
    
    string_lower = string.lower()
    substring_lower = substring.lower()
    
    i = 0
    while i < len(string):
        if string_lower[i:i+len(substring)] == substring_lower:
            modified_string += replacement
            replacements_made += 1
            i += len(substring)
        else:
            modified_string += string[i]
            i += 1
    
    return modified_string, replacements_made