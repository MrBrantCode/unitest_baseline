"""
QUESTION:
Create a function `reverse_string` that takes a string as input and returns a string with the same characters in reverse order, ignoring whitespace characters, punctuation marks, and numbers. The function should also check if the resulting string is a palindrome (reads the same forwards and backwards) and append the word "PALINDROME" at the end of the output string if it is. The function should only use built-in string methods and functions.
"""

def reverse_string(text):
    # Remove whitespace and punctuation marks
    text = ''.join(char for char in text if char.isalnum())
    
    # Remove numbers
    text = ''.join(char for char in text if not char.isdigit())
    
    # Reverse the string
    reversed_text = text[::-1]
    
    # Check if the reversed string is a palindrome
    if reversed_text.lower() == reversed_text.lower()[::-1]:
        reversed_text += " PALINDROME"
    
    return reversed_text