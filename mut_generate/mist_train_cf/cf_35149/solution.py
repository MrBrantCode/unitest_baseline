"""
QUESTION:
Create a `Decoder` class with a `decode` method that takes a string of lowercase alphabets as input and returns the decoded output by replacing "abc" with "x", "def" with "y", and "ghi" with "z", while keeping all other characters unchanged. The decoding should be case-sensitive.
"""

def decode(input_string):
    decoded_output = input_string.replace("abc", "x").replace("def", "y").replace("ghi", "z")
    return decoded_output