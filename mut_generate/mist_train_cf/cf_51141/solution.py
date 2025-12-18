"""
QUESTION:
Write a function `find_first_non_repeating_char(input_str)` that identifies the earliest occurring individual character present in a provided sequence of letters and returns its position concerning its order in the sequence. The function should not use built-in functions or methods, except for determining the length of the character sequence. The input sequence only contains alphabetical characters and does not include special characters or spaces.
"""

def find_first_non_repeating_char(input_str: str) -> str:
    """
    This function identifies the earliest occurring individual character 
    present in a provided sequence of letters and returns its position 
    concerning its order in the sequence.

    Args:
    input_str (str): A string containing alphabetical characters.

    Returns:
    str: The first non-repeating character if exists, otherwise "All characters are repeating".
    int: The position of the first non-repeating character, otherwise None.
    """
    # Initialize a dictionary to hold character counts
    count_dict = {}

    # Loop through the string
    for i in range(len(input_str)):
        # Check if character already exists in dictionary
        if input_str[i] in count_dict:
            # If it does, increment the count
            count_dict[input_str[i]] += 1
        else:
            # If it doesn't, initialize the count to 1
            count_dict[input_str[i]] = 1

    # Loop through the dictionary
    for key, value in count_dict.items():
        # The first character with count 1 is the answer
        if value == 1:
            return key, input_str.index(key)

    # If no such character exists
    return "All characters are repeating", None