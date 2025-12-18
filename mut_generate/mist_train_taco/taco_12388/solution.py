"""
QUESTION:
# Task
 The string is called `prime` if it cannot be constructed by concatenating some (more than one) equal strings together.

 For example, "abac" is prime, but "xyxy" is not("xyxy"="xy"+"xy").
 
 Given a string determine if it is prime or not.

# Input/Output


 - `[input]` string `s`

  string containing only lowercase English letters

 - `[output]` a boolean value

  `true` if the string is prime, `false` otherwise
"""

def is_prime_string(s: str) -> bool:
    """
    Determines if a given string is prime.

    A string is considered prime if it cannot be constructed by concatenating some (more than one) equal strings together.

    Parameters:
    s (str): The input string to check.

    Returns:
    bool: True if the string is prime, False otherwise.
    """
    return (s + s).find(s, 1) == len(s)