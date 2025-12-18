"""
QUESTION:
Write a function called `mirror_representation` that takes a string of alphanumeric characters as input and returns its reverse. The function should work with any characters that can be contained in a Python string, including special characters.
"""

def mirror_representation(sequence):
    # Calculate the reverse of the sequence
    mirrored_sequence = sequence[::-1]

    return mirrored_sequence