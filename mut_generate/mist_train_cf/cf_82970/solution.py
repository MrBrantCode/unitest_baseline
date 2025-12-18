"""
QUESTION:
Write a function `burrows_wheeler_transform(text)` that takes an alphanumeric string `text` as input and returns its Burrows-Wheeler Transform. The function should construct all rotations of the input string, sort them, and then concatenate the last character of each sorted rotation to form the output string. The input string is not guaranteed to have an 'end of string' marker.
"""

def burrows_wheeler_transform(text):
    rotations = sorted(text[i:] + text[:i] for i in range(len(text)))
    return ''.join(rotation[-1] for rotation in rotations)