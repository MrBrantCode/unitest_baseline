"""
QUESTION:
Create a function called `reverse_string` that takes a string `s` as input. The function should reverse the input string without using any built-in string reversal functions or libraries, handling strings with a maximum length of 1000 characters, including special characters and spaces. The reversed string should be printed out.
"""

def reverse_string(s):
    # Convert the string into a list of characters
    chars = list(s)
    
    # Get the length of the string
    length = len(chars)
    
    # Swap characters from the beginning and end of the list
    for i in range(length // 2):
        chars[i], chars[length - i - 1] = chars[length - i - 1], chars[i]
    
    # Convert the list of characters back into a string
    reversed_string = ''.join(chars)
    
    # Return the reversed string
    return reversed_string