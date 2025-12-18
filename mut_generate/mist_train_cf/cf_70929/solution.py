"""
QUESTION:
Write a function named `expand_alpha_numeric_range` that takes two string parameters `start` and `end`, where each string contains a combination of numbers and alphabets. The function should return a list of strings representing the expanded range. 

The input strings are expected to have a common alphabetic prefix, while the numeric part is a sequential range. For example, "1A" to "9A" should return ["1A", "2A", ..., "9A"]. If the alphabetic prefixes of `start` and `end` are different, the function should raise an exception.
"""

def expand_alpha_numeric_range(start, end):
    """
    Expand a range of alphanumeric strings.

    Args:
        start (str): The start of the range.
        end (str): The end of the range.

    Returns:
        list: A list of strings representing the expanded range.

    Raises:
        Exception: If the alphabetic prefixes of start and end are different.
    """
    prefix_start = ''.join(filter(str.isalpha, start))
    prefix_end = ''.join(filter(str.isalpha, end))

    if prefix_start != prefix_end:
        raise Exception("Prefix doesn't match")

    num_start = int(''.join(filter(str.isdigit, start)))
    num_end = int(''.join(filter(str.isdigit, end)))

    return [f'{i}{prefix_start}' for i in range(num_start, num_end+1)]