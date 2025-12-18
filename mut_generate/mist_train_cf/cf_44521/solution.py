"""
QUESTION:
Write a function `segment_and_unique_chars(s: str)` that takes a string `s` as input and returns a tuple where the first element is the number of segments in the string and the second element is a list of integers representing the count of unique characters in each segment, including punctuation marks and digits.

The input string `s` (0 <= s.length <= 300) consists of lower-case and upper-case English letters, digits or one of the following characters `"!@#$%^&*()_+-=',.:` and only contains the space character `' '`. A segment is defined to be a contiguous sequence of non-space characters.
"""

def segment_and_unique_chars(s: str):
    if s=="":
        return (0, [])
        
    segments = s.split(' ')
    segment_count = len(segments)
    unique_char_counts = [len(set(segment)) for segment in segments]
    return (segment_count, unique_char_counts)