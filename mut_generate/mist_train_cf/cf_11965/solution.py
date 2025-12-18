"""
QUESTION:
Generate a sequence of strings of a given length according to a specific pattern. The sequence starts with the string "1" and each subsequent string is created by concatenating the previous string with its length. The function should be named `generate_sequence(n)` and should return a list of strings where n is the number of strings in the sequence. The function should not take any other parameters besides n.
"""

def generate_sequence(n):
    sequence = ['1']
    while len(sequence) < n:
        sequence.append(sequence[-1] + str(len(sequence)))
    return sequence