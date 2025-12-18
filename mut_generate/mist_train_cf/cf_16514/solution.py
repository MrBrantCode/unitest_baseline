"""
QUESTION:
Write a function `longest_substring` that finds the longest substring of a given string with the following conditions: 
- The substring must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.
- The substring cannot contain any repeating characters.
"""

def longest_substring(s):
    """
    Finds the longest substring of a given string that contains at least one uppercase letter, 
    one lowercase letter, one digit, and one special character, and does not contain any repeating characters.

    Args:
        s (str): The input string.

    Returns:
        str: The longest substring that satisfies the conditions.
    """
    def check(s):
        if (any(c.islower() for c in s) 
            and any(c.isupper() for c in s) 
            and any(c.isdigit() for c in s) 
            and any(not c.isalnum() for c in s) 
            and len(set(s)) == len(s)):
            return True
        return False

    max_len = 0
    max_str = ""
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            sub = s[i:j]
            if check(sub) and len(sub) > max_len:
                max_len = len(sub)
                max_str = sub

    return max_str