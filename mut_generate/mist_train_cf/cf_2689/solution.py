"""
QUESTION:
Write a function `find_last_occurrence` that finds the index of the last occurrence of a given substring in a string, ignoring any occurrences that are preceded by a specified character and followed by another specified character. If the substring does not exist in the string or all occurrences are preceded by the specified character and followed by the specified character, return -1.
"""

def find_last_occurrence(string, sub_string, char_before, char_after):
    """
    Finds the index of the last occurrence of a given substring in a string, 
    ignoring any occurrences that are preceded by a specified character and 
    followed by another specified character.

    Args:
        string (str): The main string to search in.
        sub_string (str): The substring to search for.
        char_before (str): The character that should not precede the substring.
        char_after (str): The character that should not follow the substring.

    Returns:
        int: The index of the last occurrence of the substring. Returns -1 if the 
             substring does not exist in the string or all occurrences are preceded 
             by the specified character and followed by the specified character.
    """

    # Initialize the last occurrence index to -1
    last_occurrence = -1

    # Iterate over the string from the end to the beginning
    for i in range(len(string) - len(sub_string), -1, -1):
        # Check if the substring matches at the current position
        if string[i:i + len(sub_string)] == sub_string:
            # Check if the substring is not preceded by the specified character
            if i == 0 or string[i - 1] != char_before:
                # Check if the substring is not followed by the specified character
                if i + len(sub_string) == len(string) or string[i + len(sub_string)] != char_after:
                    # Update the last occurrence index
                    last_occurrence = i
                    # Break the loop as we've found the last occurrence
                    break

    return last_occurrence