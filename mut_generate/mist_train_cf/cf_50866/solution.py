"""
QUESTION:
Write a function `compress_string` that compresses a given string into its smallest form by replacing sequences of repeating characters with a single character and the count of consecutive repetitions, but only if the resulting string is smaller than the original string. The function should take an input string as an argument and return the compressed string.
"""

def compress_string(s):
    """
    Compress a string by replacing sequences of repeating characters with a single character and the count of consecutive repetitions.

    Args:
        s (str): The input string to be compressed.

    Returns:
        str: The compressed string.
    """
    if not s:
        return s

    compressed_string = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed_string += s[i - 1] + str(count)
            count = 1

    compressed_string += s[-1] + str(count)

    return compressed_string if len(compressed_string) < len(s) else s