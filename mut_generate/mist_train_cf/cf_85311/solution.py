"""
QUESTION:
Write a function `find_least_common` that reads a series of alphanumeric characters from either a raw string or a file and returns the least common alphanumeric character and the line in which it first appears if read from a file. 

The function should ignore non-alphanumeric characters and handle ties by choosing the character with the smallest ASCII value. It should also provide a user-friendly error message if a file does not exist or if there is an error reading the input.

Note that the function should be case-insensitive and it should only read the file once.
"""

from collections import Counter

def find_least_common(source):
    """
    Reads a series of alphanumeric characters from either a raw string or a file 
    and returns the least common alphanumeric character and the line in which it 
    first appears if read from a file.

    Args:
        source (str or file object): The input source.

    Returns:
        tuple: A tuple containing the least common character and the line number 
        if read from a file, otherwise None.
    """

    if isinstance(source, str):
        text = source
        lines = None
    else:
        lines = source.readlines()
        text = ''.join(lines)

    counter = Counter(char.lower() for char in text if char.isalnum())
    min_count = min(counter.values())
    least_common_chars = [char for char, count in counter.items() if count == min_count]
    min_ascii = min(least_common_chars, key=ord)

    if lines is not None:
        for i, line in enumerate(lines):
            if min_ascii in line.lower():
                return min_ascii, i + 1
    return min_ascii, None