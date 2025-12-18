"""
QUESTION:
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
"""

def count_segments(s: str) -> int:
    """
    Count the number of segments in a string, where a segment is defined as a contiguous sequence of non-space characters.

    Parameters:
    s (str): The input string to count segments in.

    Returns:
    int: The number of segments in the string.
    """
    return len(s.split())