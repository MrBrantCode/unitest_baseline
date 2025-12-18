"""
QUESTION:
Write a function named `count_fingers` that takes a string of ASCII art as input and returns the number of fingers represented by the gesture. The ASCII art uses the following characters: `)` for the base of the thumb, ` ` (space) for the palm, `d` for a bent finger, and `o` for a straight finger. Fingers are counted from left to right, with each finger represented by the sequence `do` or `o`, and the thumb always being straight and represented by `o`.
"""

def count_fingers(ascii_art):
    fingers = 0
    finger_sequence = ''
    for line in ascii_art.split('\n'):
        for char in line:
            if char == 'd' or char == 'o':
                finger_sequence += char
            elif char == ')':
                if finger_sequence:
                    fingers += 1
                    finger_sequence = ''
    return fingers