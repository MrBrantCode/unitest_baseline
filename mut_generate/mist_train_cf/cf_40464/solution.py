"""
QUESTION:
Create a function called `transform_ascii_art` that takes a multi-line string representing an ASCII art as input. The function should perform a transformation on the ASCII art by first rotating it 90 degrees clockwise and then flipping it horizontally. The output should be the transformed ASCII art as a string. The input string will contain only ASCII characters and newline characters.
"""

def transform_ascii_art(ascii_art):
    lines = ascii_art.strip().split('\n')
    rotated_art = [''.join([lines[j][i] for j in range(len(lines)-1, -1, -1)]) for i in range(len(lines[0]))]
    flipped_art = '\n'.join(reversed(rotated_art))  # Reversed is added here to flip the lines horizontally
    return flipped_art