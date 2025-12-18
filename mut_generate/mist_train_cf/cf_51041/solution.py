"""
QUESTION:
Design a function named `convert_and_reverse` that takes a string input, changes every third character to upper-case letters, reverses the order of these characters, and returns the resulting string. The function should handle any exceptions and errors that may occur during execution, and instead of crashing, it should return a friendly error message. The input string is assumed to be a user-inputted string.
"""

def convert_and_reverse(s):
    try:
        new_string = ''
        for i in range(len(s)):
            if (i+1) % 3 == 0:
                new_string += s[i].upper()
            else:
                new_string += s[i]
        return new_string[::-1]
    except Exception as e:
        return f"An error occurred: {str(e)}"