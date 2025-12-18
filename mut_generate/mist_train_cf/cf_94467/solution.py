"""
QUESTION:
Implement a function called `determine_string_type(input_string)` that determines the type of the input string. The function should check the following conditions in order: 
- empty string
- numeric string
- alphabetic string
- alphanumeric string
- proper noun (starts with an uppercase letter and has only alphabetical characters afterwards)
- palindrome
If none of the above conditions are met, return "Unknown type".
"""

def determine_string_type(input_string):
    if input_string == "":
        return "Empty string"
    elif input_string.isdigit():
        return "Numeric string"
    elif input_string.isalpha():
        return "Alphabetic string"
    elif input_string.isalnum():
        return "Alphanumeric string"
    elif input_string[0].isupper() and input_string[1:].isalpha():
        return "Proper noun"
    elif input_string == input_string[::-1]:
        return "Palindrome"
    else:
        return "Unknown type"