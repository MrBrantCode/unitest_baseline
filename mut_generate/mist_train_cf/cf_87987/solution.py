"""
QUESTION:
Create a function `is_palindrome(string)` that takes a string as input and returns "Palindrome" if the string is a palindrome, ignoring case and non-alphanumeric characters, and "Not a palindrome" otherwise.
"""

def entrance(string):
    # Convert the string to lowercase
    string = string.lower()
    
    # Remove non-alphanumeric characters
    string = ''.join(char for char in string if char.isalnum())
    
    # Check if the string is equal to its reverse
    if string == string[::-1]:
        return "Palindrome"
    else:
        return "Not a palindrome"