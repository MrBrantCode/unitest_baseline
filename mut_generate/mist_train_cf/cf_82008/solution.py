"""
QUESTION:
Find the positions of two characters in a string and the distance between them in the opposite direction when the string is considered a circular array. The function `find_positions_and_distance(text, char1, char2)` should take a string `text`, and two characters `char1` and `char2` as input, and return a tuple containing the positions of `char1` and `char2` and their distance in the opposite direction. Assume that string indexes start from 0.
"""

def find_positions_and_distance(text, char1, char2):
    pos1 = text.find(char1)
    pos2 = text.find(char2)
    
    # Calculate distance in the opposite direction
    max_pos = max(pos1, pos2)
    min_pos = min(pos1, pos2)
    forward_distance = max_pos - min_pos
    backward_distance = len(text) - forward_distance
    
    return (pos1, pos2, backward_distance)