"""
QUESTION:
Create a function named `verify_string` that takes an input string and returns the string if it starts with 'a' and ends with 'e', contains only unique and sequential lowercase letters 'a' through 'e', and no other characters. If the string does not match these conditions, the function should return 'No match'. The function must not use built-in regular expression libraries or functions.
"""

def verify_string(input_string):
    # Check if string starts with 'a' and ends with 'e':
    if input_string[0] != 'a' or input_string[-1] != 'e':
        return 'No match'
    
    # Check if all characters are sequential:
    for i in range(len(input_string) - 1):  
        if ord(input_string[i + 1]) - ord(input_string[i]) != 1:
            return 'No match'
        
    # Check if all characters are distinct:
    if len(input_string) != len(set(input_string)):
        return 'No match'
        
    # If all conditions are fulfilled, return the valid input string:
    return input_string