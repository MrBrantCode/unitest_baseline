"""
QUESTION:
Create a class called `StringAnalyzer` that takes a string as input. The class should have methods to return the length of the string, reverse the string, and check whether the string is a palindrome (ignoring spaces, punctuation, and capitalization). The palindrome check should be case-insensitive and consider only alphanumeric characters.
"""

def entrance(s):
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned_string == cleaned_string[::-1]