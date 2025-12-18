"""
QUESTION:
Find the start of a repeating pattern in a stream of numbers. The function, `find_pattern`, should take an array of integers as input and return a tuple containing the pattern and its starting index. The pattern is defined as the longest sequence of numbers that repeats at least once in the stream.
"""

def find_pattern(stream):
    length = len(stream)
    for pattern_length in range(1, length // 2 + 1):
        if length % pattern_length == 0:
            pattern = stream[:pattern_length]
            if pattern * (length // pattern_length) == stream:
                return (pattern, 0)
    return None