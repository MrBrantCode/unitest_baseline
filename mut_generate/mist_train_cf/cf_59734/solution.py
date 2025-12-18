"""
QUESTION:
Write a function `consecutiveLetters` that takes a list of strings as input, removes all special characters, digits, and trailing spaces from each string, and returns the modified list sorted in descending order based on the highest possible number of consecutive letters in each string. Do not use any external libraries or built-in string methods. Implement your own functions for character and string manipulations.
"""

def consecutiveLetters(strings):
    """
    This function takes a list of strings as input, removes all special characters, 
    digits, and trailing spaces from each string, and returns the modified list 
    sorted in descending order based on the highest possible number of consecutive 
    letters in each string.

    Args:
        strings (list): A list of strings.

    Returns:
        list: The modified list sorted in descending order based on the highest 
        possible number of consecutive letters in each string.
    """

    def is_alpha(char):
        """Checks if a character is a letter."""
        return ('A' <= char <= 'Z') or ('a' <= char <= 'z')

    def remove_special_chars(s):
        """Removes all special characters, digits, and trailing spaces from a string."""
        result = ''
        for char in s:
            if is_alpha(char) or char == ' ':
                result += char
        return result.strip()

    def count_consecutive_letters(s):
        """Counts the highest possible number of consecutive letters in a string."""
        max_count = 0
        current_count = 0
        for char in s:
            if is_alpha(char):
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
        return max_count

    # Remove special characters from each string
    cleaned_strings = [remove_special_chars(s) for s in strings]

    # Sort the strings based on the highest possible number of consecutive letters
    sorted_strings = sorted(cleaned_strings, key=count_consecutive_letters, reverse=True)

    return sorted_strings