"""
QUESTION:
Create a function named `isPalindrome(s)` that takes a string `s` as input and returns `True` if the string is a palindrome, `False` otherwise, or "empty string" if the string is empty after removing whitespace. The function should not use Python's built-in functions or external libraries and should optimize for time and space complexity. It should also handle edge cases such as empty strings and white spaces. 

Additionally, the function should be used to validate two input strings and their concatenation in both orders.
"""

def isPalindrome(s): 
    # Removing whitespace
    s = s.replace(' ', '')
    
    # Checking if string is empty
    if s == "":
        # Return "empty string" instead of True or False
        return "empty string"

    length = 0
    for character in s:
        length += 1

    i = 0
    while i < length // 2:
        if s[i] != s[length - i - 1]:
            return False
        i += 1

    return True