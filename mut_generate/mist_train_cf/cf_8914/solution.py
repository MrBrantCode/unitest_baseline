"""
QUESTION:
Write a function called `remove_whitespace_and_reverse` that takes a string as input, removes all whitespace characters, and returns the resulting string in reverse order. The function should handle strings with multiple consecutive whitespace characters and not include any whitespace in the output.
"""

def remove_whitespace_and_reverse(string):
    # Remove whitespace characters using the replace() method
    string = string.replace(" ", "")
    
    # Reverse the string using slicing with step -1
    string = string[::-1]
    
    return string