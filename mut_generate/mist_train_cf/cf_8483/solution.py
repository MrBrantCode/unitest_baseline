"""
QUESTION:
Implement a function `countCharacters` that takes a string as input and outputs the count of all alphabetic characters (both lowercase and uppercase) in the string, excluding any special characters. The function should handle uppercase and lowercase letters as separate characters and have a time complexity of O(n) and space complexity of O(1), where n is the length of the string. Implement this using only a single loop and without using any built-in functions or libraries for counting characters.
"""

def countCharacters(s: str) -> int:
    """
    This function takes a string as input and outputs the count of all alphabetic characters 
    (both lowercase and uppercase) in the string, excluding any special characters.

    Parameters:
    s (str): The input string.

    Returns:
    int: The count of all alphabetic characters in the string.
    """

    count = 0
    for char in s:
        # Check if the character is an alphabet (both lowercase and uppercase)
        if (ord('a') <= ord(char) <= ord('z')) or (ord('A') <= ord(char) <= ord('Z')):
            count += 1
    return count