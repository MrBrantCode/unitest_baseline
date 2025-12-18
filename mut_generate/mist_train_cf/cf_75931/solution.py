"""
QUESTION:
Construct a function `construct_string` that generates a sequence of a given length containing only the letters 'x', 'y', and 'z'. The sequence must follow a pattern where 'x', 'y', and 'z' occur at least once in every group of four characters. The function should run in linear time or better and handle cases where the length is not a multiple of 4.
"""

def construct_string(length):
    subsequence = 'xyzx'
    sequence = subsequence * (length // len(subsequence))
    remaining = length % len(subsequence)
    if remaining:
        sequence += subsequence[:remaining]
    return sequence