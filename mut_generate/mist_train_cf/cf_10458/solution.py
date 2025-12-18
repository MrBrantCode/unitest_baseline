"""
QUESTION:
Write a function named `isSubstring` that takes two strings `string1` and `string2` as inputs and returns a boolean indicating whether `string2` is a substring of `string1`. The function should handle cases where `string2` contains multiple occurrences of characters from `string1`. Assume that both strings only contain lowercase English letters.
"""

def isSubstring(string1, string2):
    """
    Checks if string2 is a substring of string1.

    Args:
    string1 (str): The main string.
    string2 (str): The substring to check.

    Returns:
    bool: True if string2 is a substring of string1, False otherwise.
    """
    count1 = [0] * 26  # Array to store the count of each character in string1
    count2 = [0] * 26  # Array to store the count of each character in string2

    # Calculate the count of each character in string1
    for char in string1:
        count1[ord(char) - ord('a')] += 1

    # Calculate the count of each character in string2
    for char in string2:
        count2[ord(char) - ord('a')] += 1

    # Check if string2 is a substring of string1
    for i in range(26):
        # If the count of a character in string2 is greater than the count of that character in string1, return False
        if count2[i] > count1[i]:
            return False

    return True