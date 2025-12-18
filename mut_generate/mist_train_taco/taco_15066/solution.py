"""
QUESTION:
Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

str.isalnum() 

This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

>>> print 'ab123'.isalnum()
True
>>> print 'ab123#'.isalnum()
False

str.isalpha() 

This method checks if all the characters of a string are alphabetical (a-z and A-Z).

>>> print 'abcD'.isalpha()
True
>>> print 'abcd1'.isalpha()
False

str.isdigit() 

This method checks if all the characters of a string are digits (0-9).

>>> print '1234'.isdigit()
True
>>> print '123edsd'.isdigit()
False

str.islower() 

This method checks if all the characters of a string are lowercase characters (a-z).

>>> print 'abcd123#'.islower()
True
>>> print 'Abcd123#'.islower()
False

str.isupper() 

This method checks if all the characters of a string are uppercase characters (A-Z).

>>> print 'ABCD123#'.isupper()
True
>>> print 'Abcd123#'.isupper()
False

Task

You are given a string $\mbox{S}$. 

Your task is to find out if the string $\mbox{S}$ contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters. 

Input Format

A single line containing a string $\mbox{S}$.

Constraints

$0<len(S)<1000$

Output Format

In the first line, print True if $\mbox{S}$ has any alphanumeric characters. Otherwise, print False. 

In the second line, print True if $\mbox{S}$ has any alphabetical characters. Otherwise, print False. 

In the third line, print True if $\mbox{S}$ has any digits. Otherwise, print False. 

In the fourth line, print True if $\mbox{S}$ has any lowercase characters. Otherwise, print False. 

In the fifth line, print True if $\mbox{S}$ has any uppercase characters. Otherwise, print False.  

Sample Input
qA2

Sample Output
True
True
True
True
True
"""

def validate_string(s: str) -> tuple:
    """
    Validates the input string based on various criteria.

    Parameters:
    s (str): The input string to be validated.

    Returns:
    tuple: A tuple containing five boolean values:
           1. True if s contains any alphanumeric characters, otherwise False.
           2. True if s contains any alphabetical characters, otherwise False.
           3. True if s contains any digits, otherwise False.
           4. True if s contains any lowercase characters, otherwise False.
           5. True if s contains any uppercase characters, otherwise False.
    """
    return (
        any(char.isalnum() for char in s),
        any(char.isalpha() for char in s),
        any(char.isdigit() for char in s),
        any(char.islower() for char in s),
        any(char.isupper() for char in s)
    )