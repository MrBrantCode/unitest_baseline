"""
QUESTION:
Create a function `clean_and_count_vowels` that takes a string as input. The function should convert the input string to lowercase, remove any non-alphanumeric characters, and return the cleaned string along with the count of vowels in the cleaned string.
"""

def clean_and_count_vowels(input_string):
    """
    This function takes a string as input, converts it to lowercase, removes any non-alphanumeric characters, 
    and returns the cleaned string along with the count of vowels in the cleaned string.

    Args:
        input_string (str): The input string to be cleaned and counted for vowels.

    Returns:
        tuple: A tuple containing the cleaned string and the count of vowels in the cleaned string.
    """

    # Convert string to lowercase
    lowercase_string = input_string.lower()

    # Remove special characters
    clean_string = ''.join(e for e in lowercase_string if e.isalnum())

    # Count number of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = sum(1 for char in clean_string if char in vowels)

    return clean_string, count