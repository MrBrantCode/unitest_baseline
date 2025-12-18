"""
QUESTION:
Write a function `expand_strings` that takes a list of strings as input. For each string in the list, create a set of characters if the string contains at least one vowel and consists only of letters. Ignore strings that contain special characters or numbers. Return a list of tuples, where each tuple contains the original string and its corresponding set of characters sorted in descending order based on the number of vowels.

The function should meet the following requirements:

- Input: `string_list` (1 <= len(string_list) <= 10^4) is a list of strings, where each string contains at least one character and consists only of uppercase and lowercase letters, and whitespace.
- Output: A list of tuples, where each tuple contains the original string and its corresponding set of characters sorted in descending order based on the number of vowels.
- The resulting sets of characters should be sorted in descending order based on the number of vowels.
- All characters in the input strings are letters and whitespace.
"""

def expand_strings(string_list):
    """
    This function takes a list of strings, creates a set of characters if the string contains at least one vowel and consists only of letters,
    and returns a list of tuples, where each tuple contains the original string and its corresponding set of characters sorted in descending order based on the number of vowels.

    Args:
        string_list (list): A list of strings.

    Returns:
        list: A list of tuples, where each tuple contains the original string and its corresponding set of characters.
    """

    # Define the set of vowels
    vowels = set('aeiouAEIOU')

    # Initialize an empty list to store the result
    result = []

    # Iterate over each string in the input list
    for string in string_list:
        # Check if the string contains at least one vowel and consists only of letters and whitespace
        if any(char in vowels for char in string) and string.replace(' ', '').isalpha():
            # Create a set to store the characters of the string
            chars = set(string.replace(' ', ''))

            # Append a tuple containing the string and its set of characters to the result list
            result.append((string, chars))

    # Sort the result list in descending order based on the number of vowels in each set of characters
    result.sort(key=lambda x: len(x[1] & vowels), reverse=True)

    return result