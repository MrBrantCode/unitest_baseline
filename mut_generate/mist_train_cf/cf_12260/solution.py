"""
QUESTION:
Write a function `is_greater` that takes two strings as input and returns a boolean indicating whether the first string is lexicographically greater than the second string in a case-sensitive comparison without using any built-in string comparison functions or libraries.
"""

def is_greater(str1, str2):
    # Check if the length of str1 is greater than the length of str2
    if len(str1) > len(str2):
        return True
    # Check if the length of str1 is less than the length of str2
    elif len(str1) < len(str2):
        return False
    else:
        # Iterate through each character of the strings
        for i in range(len(str1)):
            # Compare the ASCII values of the characters
            if ord(str1[i]) > ord(str2[i]):
                return True
            # If the ASCII values are equal, continue to the next character
            elif ord(str1[i]) == ord(str2[i]):
                continue
            # If the ASCII value of str1 is less than str2, return False
            else:
                return False
        # If all characters are equal, return False
        return False