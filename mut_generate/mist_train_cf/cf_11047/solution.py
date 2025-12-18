"""
QUESTION:
Create a function called `delete_non_alphanumeric` that takes a string as input. The function should remove all non-alphanumeric characters from the input string and return a new string with the remaining alphanumeric characters in reverse order. The function should maintain the case of the letters in the output string. The input string can contain upper and lowercase letters, numbers, and special characters.
"""

def delete_non_alphanumeric(s):
    return ''.join(filter(str.isalnum, s))[::-1]