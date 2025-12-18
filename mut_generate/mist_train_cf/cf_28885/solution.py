"""
QUESTION:
Implement the `modify_string` function, which takes a single parameter `input_string` (a string containing only alphabetical characters with 1-1000 characters) and returns a modified version of the string based on the following rules: 
- If the string contains only uppercase letters, convert it to lowercase and reverse.
- If the string contains only lowercase letters, convert it to uppercase and reverse.
- If the string contains a mix of uppercase and lowercase letters, capitalize the first letter of each word and reverse the order of the words.
The function should treat uppercase and lowercase letters as equivalent when determining which rule to apply.
"""

def modify_string(input_string):
    if input_string.isupper():
        return input_string.lower()[::-1]
    elif input_string.islower():
        return input_string.upper()[::-1]
    else:
        return ' '.join(word.capitalize() for word in input_string.split()[::-1])